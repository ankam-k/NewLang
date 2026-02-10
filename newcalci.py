'''print("\nGive all operand followed by operator and again operand..untill done press ENTER")
print("Give (=) in new line and press ENTER\nOUTPUT is resulted\n")
exp=""
while True:
    num=input()
    if num=="=":
        break
    exp+=num
try:
    result=eval(exp)
    print(result)
except ZeroDivisionError as e:
    print("Error: ", e)
except Exception as e:
    print("Error: ", e)'''

import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    current = entry.get()
    if button_text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
            entry.delete(0, tk.END)
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            entry.delete(0, tk.END)
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# GUI setup
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=10, sticky="we")

# Button layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "C", "+"),
    ("=",)
]

# Create buttons dynamically
for row_index, row_values in enumerate(buttons, start=1):
    for col_index, value in enumerate(row_values):
        btn = tk.Button(root, text=value, font=("Arial", 18), width=5, height=2,
                        command=lambda v=value: on_click(v))
        btn.grid(row=row_index, column=col_index, padx=5, pady=5)

root.mainloop()