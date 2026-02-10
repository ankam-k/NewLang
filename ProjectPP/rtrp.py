import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from threading import Thread
import torch
import time
import winsound

# Global settings
ALERT_CLASSES = ["person", "knife", "gun"]
model_choice = "YOLOv5"

# Kalman Filter Setup
def init_kalman():
    kalman = cv2.KalmanFilter(4, 2)
    kalman.measurementMatrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], np.float32)
    kalman.transitionMatrix = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)
    kalman.processNoiseCov = np.eye(4, dtype=np.float32) * 0.03
    return kalman

# Play alert sound
def play_alert():
    winsound.Beep(1000, 500)

# Trigger alert popup
def trigger_alert(label):
    Thread(target=play_alert).start()
    messagebox.showwarning("Alert!", f"{label} detected!")

# Load YOLOv5 Model
def load_yolo_model():
    return torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Load SSD model (OpenCV)
def load_ssd_model():
    net = cv2.dnn.readNetFromCaffe(
        'MobileNetSSD_deploy.prototxt',
        'MobileNetSSD_deploy.caffemodel'
    )
    return net

# Object Detection and Tracking

def detect_and_track(cap, model_type):
    if model_type == "YOLOv5":
        model = load_yolo_model()
    else:
        model = load_ssd_model()

    kalman = init_kalman()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if model_type == "YOLOv5":
            results = model(frame)
            for *xyxy, conf, cls in results.xyxy[0]:
                label = results.names[int(cls)]
                if label in ALERT_CLASSES:
                    trigger_alert(label)
                x1, y1, x2, y2 = map(int, xyxy)
                center = (int((x1 + x2)/2), int((y1 + y2)/2))
                prediction = kalman.predict()
                kalman.correct(np.array([[np.float32(center[0])], [np.float32(center[1])]]))
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

        else:
            blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
            model.setInput(blob)
            detections = model.forward()
            classNames = {15: "person"}  # Expand this as needed

            for i in range(detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                if confidence > 0.4:
                    idx = int(detections[0, 0, i, 1])
                    label = classNames.get(idx, "unknown")
                    if label in ALERT_CLASSES:
                        trigger_alert(label)
                    box = detections[0, 0, i, 3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
                    (startX, startY, endX, endY) = box.astype("int")
                    center = (int((startX + endX)/2), int((startY + endY)/2))
                    kalman.correct(np.array([[np.float32(center[0])], [np.float32(center[1])]]))
                    prediction = kalman.predict()
                    cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)
                    cv2.putText(frame, label, (startX, startY - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        cv2.imshow("GuardianEye Pro", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# GUI Functions
def browse_video():
    path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi")])
    if path:
        cap = cv2.VideoCapture(path)
        Thread(target=detect_and_track, args=(cap, model_choice)).start()

def start_webcam():
    cap = cv2.VideoCapture(0)
    Thread(target=detect_and_track, args=(cap, model_choice)).start()

def set_model(choice):
    global model_choice
    model_choice = choice

# GUI Setup
def launch_gui():
    root = tk.Tk()
    root.title("GuardianEye Pro")
    root.geometry("400x300")

    tk.Label(root, text="GuardianEye Pro", font=("Arial", 16, "bold")).pack(pady=10)

    tk.Button(root, text="Browse Video File", width=25, command=browse_video).pack(pady=5)
    tk.Button(root, text="Start Webcam Surveillance", width=25, command=start_webcam).pack(pady=5)

    tk.Label(root, text="Select Detection Model:").pack(pady=10)
    combo = ttk.Combobox(root, values=["YOLOv5", "SSD"], state="readonly")
    combo.current(0)
    combo.bind("<<ComboboxSelected>>", lambda e: set_model(combo.get()))
    combo.pack()

    tk.Label(root, text="Alert for: person, knife, gun", fg="gray").pack(pady=10)

    root.mainloop()

launch_gui()
