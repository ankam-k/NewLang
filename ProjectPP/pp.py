# importing different modules
import threading
import time
import calendar
import os

#creating a file to store original data
FILENAME = "booking_data.txt"

def info():
  ''' 
  We are presenting ticket booking application in python language taking example of TTD(Tirumala Tirupati Devasthanams)
  Darshan booking by importing different modules, mainly using thread module here, by creating various threads to funtion
  concurrently.
  '''
  print(info.__doc__)

#creating menu to display the application
def menu():
  tab=input("\nStart the application by pressing underscore(_)\n")
  while True:
    if tab=="_":
      print("\n\nTirumala Tirupati Devasthanams\n...Ticket Booking...\n")
      print("1. Book\n2. Booking Details/History\n3. Cancel\n4. Exit\n")
      opt=int(input("Select option: "))
      if opt==1:
        objPay.date()
        objPay.Type()
        objPay.check()
        objPay.payCheck()
        time.sleep(2)
      elif opt==2:
        objPay.printDetails()
        time.sleep(2)
      elif opt==3:
        objCancel.cancel()
        time.sleep(2)
      elif opt==4:
        print("Exiting the application!!\nThank You:)\n")
        break
      else:
        print("Invalid Option. Please try again..")
        time.sleep(2)
    else:
      pass

#creating a class for entry of date
class Date:
  def date(self):
    self.n=int(input("Enter number of persons: "))
    self.yy=int(input("Year(2024-2030) of booking: "))
    self.mm=int(input("Month(01-12) of booking: "))
    print("\n")
    print(calendar.month(self.yy,self.mm))
    self.dd=int(input("Enter date of booking: "))
    print(f"Your Booking Date is {self.dd}/{self.mm}/{self.yy}..")
    self.conf=input("Confirm it - 'Yes' or 'No' : ")
    if self.conf=="Yes":
      objPay.Type()
      pass
    else:
      return self.date()

#child class of (Date) for checking availability of tickets
class Check(Date):
  def check(self):
    print("\nChecking Availability..")
    time.sleep(1)
    print("Please wait!")
    time.sleep(2)
    checkThread=threading.Thread(target=self.avail) # thread for checking availability
    checkThread.start()
    checkThread.join()
  def avail(self):
    self.tickets=10
    if self.tickets>=self.n:
      print("\nAvailable\n")
      time.sleep(1)
    else:
        print("\nUnavailable\n")
        inp=input("Check for another date - 'Yes' or 'No' : ")
        if inp=="Yes":
          objPay.date()
          objPay.check()
        else:
          print("Thank you..")
          time.sleep(2)
          print("Exiting..")
          time.sleep(2)
          print("Successfully logged out.!")

#creating a child class of (Check) to proceed for booking and storing it in file
class Book(Check):
  def __init__(self):
    self.booking=[] # initialising list to store bookings

  def saveToFile(self, bookingData):
    with open(FILENAME, "a") as file:
      dataStr="\t".join(map(str, bookingData))+"\n"
      file.write(dataStr)

  def bookInfo(self):
    self.bookingList=[]
    for i in range(self.n):
      print("\nEnter the info for person", i+1, ":")
      self.name=input("Name: ")
      self.age=int(input("Age: "))
      self.mobile=int(input("Mobile Number: "))
      self.bookID=i+1
      print("Your booking ID is ", self.bookID)
      self.bookingData= [self.bookID, self.name, self.age, self.mobile, f"{self.dd}/{self.mm}/{self.yy}" ]
      self.bookingList.append(self.bookingData)
    print("\nInfo Saved!!\n")
    
  def printDetails(self):
    print("Booking Details:\n")
    print("ID\tName\tAge\tMobile No.\tDate\tType")
    with open(FILENAME, "r") as file:
      for line in file:
        print(line.strip())

  def Darshan(self):
    self.bookInfo()
    self.darshanSlot=100
    print("\na. Sarva Darshan\nb. Special Entry Darshan\nc. VIP Darshan")
    self.darsh=input("Darshan Type: ")
    if self.darsh=="a":
      darshanType=["Sarva Darshan"]
    elif self.darsh=="b":
      payment=300
      print("Payment = ", (payment*self.n), "/- Rs")
      darshanType=["Special Entry Darshan"]
    elif self.darsh=="c":
      payment=1000
      print("Payment = ", (payment*self.n), "/- Rs")
      darshanType=["VIP Darshan"]
    else:
      print("Try again!")
    bookThreads=[]
    for self.bookingData in self.bookingList:
      self.bookingData.extend(darshanType)
      #self.saveToFile(bookingData) -> a simple line instead of using the below lines
      bookThread=threading.Thread(target=self.saveToFile, args=(self.bookingData,))
      bookThreads.append(bookThread) # thread for booking details info to store
      bookThread.start()
    for thread in bookThreads: # here thread takes bookThread as parameter to print the data in a loop
      thread.join()
    self.darshanSlot-=self.n
    #print("Remaining slots are ", self.darshanSlot)
  def Accomodation(self):
    self.bookInfo()
    self.accommodationSlot=100
    print("\na. Free Accommodation\nb. Budget Accommodation\nc. Standard Accommodation\nd. Deluxe Accommodation\ne. Suite")
    self.accommodationType = input("Accommodation Type: ")
    if self.accommodationType == "a":
      accType = ["Free Accommodation"]
    elif self.accommodationType == "b":
      payment = 500
      print("Payment = ", (payment * self.n), "/- Rs")
      accType = ["Budget Accommodation"]
    elif self.accommodationType == "c":
      payment = 1000
      print("Payment = ", (payment * self.n), "/- Rs")
      accType = ["Standard Accommodation"]
    elif self.accommodationType == "d":
      payment = 2000
      print("Payment = ", (payment * self.n), "/- Rs")
      accType = ["Deluxe Accommodation"]
    elif self.accommodationType == "e":
      payment = 5000
      print("Payment = ", (payment * self.n), "/- Rs")
      accType = ["Suite"]
    else:
      return
    bookThreads = []
    for self.bookingData in self.bookingList:
      self.bookingData.extend(accType)
      bookThread = threading.Thread(target=self.saveToFile, args=(self.bookingData,))
      bookThreads.append(bookThread)  # thread for booking details info to store
      bookThread.start()
    for thread in bookThreads:  # here thread takes bookThread as parameter to print the data in a loop
      thread.join()
    self.accommodationSlot -= self.n
    #print("Remaining slots are ", self.accomodationSlot)
  def Seva(self):
    self.bookInfo()
    self.sevaSlot = 50
    print("\na. Suprabhatam Seva\nb. Tomala Seva\nc. Archana Seva\nd. Vasanthotsavam\ne. Kalyanotsavam\nf. Arjitha Brahmotsavam\ng. Dolotsavam (Unjal Seva)\nh. Sahasra Deepalankarana Seva\ni. Nijapada Darshanam\nj. Vishesha Pooja")
    self.sevaType = input("Seva Type: ")
    if self.sevaType == "a":
      sevaType = ["Suprabhatam Seva"]
    elif self.sevaType == "b":
      sevaType = ["Tomala Seva"]
    elif self.sevaType == "c":
      sevaType = ["Archana Seva"]
    elif self.sevaType == "d":
      sevaType = ["Vasanthotsavam"]
    elif self.sevaType == "e":
      sevaType = ["Kalyanotsavam"]
    elif self.sevaType == "f":
      sevaType = ["Arjitha Brahmotsavam"]
    elif self.sevaType == "g":
      sevaType = ["Dolotsavam (Unjal Seva)"]
    elif self.sevaType == "h":
      sevaType = ["Sahasra Deepalankarana Seva"]
    elif self.sevaType == "i":
      sevaType = ["Nijapada Darshanam"]
    elif self.sevaType == "j":
      sevaType = ["Vishesha Pooja"]
    else:
      return
    bookThreads = []
    for self.bookingData in self.bookingList:
      self.bookingData.extend(sevaType)
      bookThread = threading.Thread(target=self.saveToFile, args=(self.bookingData,))
      bookThreads.append(bookThread)  # thread for booking details info to store
      bookThread.start()
    for thread in bookThreads:  # here thread takes bookThread as parameter to print the data in a loop
      thread.join()
    self.sevaSlot -= self.n
    #print("Remaining slots are ", self.sevaSlot)
  def Kalyanam(self):
    self.bookInfo()
    self.kalyanamSlot = 50
    print("\na. Srivari Kalyanam\nb. Srivaru Parinayotsavam\nc. Pavitra Kalyanam\nd. Vasantha Kalyanam")
    self.kalyanamType = input("Kalyanam Type: ")
    if self.kalyanamType == "a":
      payment = 1000
      print("Payment = ", (payment * self.n), "/- Rs")
      kalyanamType = ["Srivari Kalyanam"]
    elif self.kalyanamType == "b":
      payment = 1500
      print("Payment = ", (payment * self.n), "/- Rs")
      kalyanamType = ["Srivaru Parinayotsavam"]
    elif self.kalyanamType == "c":
      payment = 2000
      print("Payment = ", (payment * self.n), "/- Rs")
      kalyanamType = ["Pavitra Kalyanam"]
    elif self.kalyanamType == "d":
      payment = 2500
      print("Payment = ", (payment * self.n), "/- Rs")
      kalyanamType = ["Vasantha Kalyanam"]
    else:
      return
    bookThreads = []
    for self.bookingData in self.bookingList:
      self.bookingData.extend(kalyanamType)
      bookThread = threading.Thread(target=self.saveToFile, args=(self.bookingData,))
      bookThreads.append(bookThread)  # thread for booking details info to store
      bookThread.start()
    for thread in bookThreads:  # here thread takes bookThread as parameter to print the data in a loop
      thread.join()
    self.kalyanamSlot -= self.n
    #print("Remaining slots are ", self.kalyanamSlot)
  def Type(self):
    print("A. Darshan Booking\nB. Accomodation Booking\nC. Seva Booking\nD. Kalyanam Booking")
    self.Bookie=input("\nSelect booking type:")
    if self.Bookie=="A":
      darshanThread=threading.Thread(target=self.Darshan)
      darshanThread.start()
      darshanThread.join()
    elif self.Bookie=="B":
      accomThread=threading.Thread(target=self.Accomodation)
      accomThread.start()
      accomThread.join()
    elif self.Bookie=="C":
      sevaThread=threading.Thread(target=self.Seva)
      sevaThread.start()
      sevaThread.join()
    elif self.Bookie=="D":
      kalyanamThread=threading.Thread(target=self.Kalyanam)
      kalyanamThread.start()
      kalyanamThread.join()
    else:
      pass

#creating first child class of (Book) for payment process
class Pay(Book):
  def payment(self):
    time.sleep(1)
    selc=int(input("Select mode of payment: "))
    if selc==1 or selc==2 or selc==3 or selc==4 or selc==5:
      payThread=threading.Thread(target=self.payProcessing) # creation of thread for payment process
      recThread=threading.Thread(target=self.genReceipt) # creation of thread for generation of receipt
      payThread.start()
      recThread.start()
      payThread.join()
      recThread.join()
    else:
      print("Incorrect payment method..")
      self.payMenu()

  def payCheck(self):
    if hasattr(self, 'darsh') and self.darsh in ["a"]:
      print("\nBooking successful..")
      self.genReceipt()
      time.sleep(2)
    elif hasattr(self, 'accommodationType') and self.accommodationType in ["a"]:
      print("\nBooking successful..")
      self.genReceipt()
      time.sleep(2)
    elif hasattr(self, 'sevaType') and self.sevaType in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]:
      print("\nBooking successful..")
      self.genReceipt()
      time.sleep(2)
    else:
      time.sleep(1)
      print("Proceed to Pay..\n")
      time.sleep(1)
      objPay.payMenu()
      objPay.payment()

  def payMenu(self):
    print("\n1. PhonePe, GPay\n2. UPI\n3. Net Banking\n4. Credit Card\n5. Debit Card\n")
  def payProcessing(self):
    print("\nPayment Processing..")
    time.sleep(1) # processing of payment
    print("Payment Successful..!\n")
  def genReceipt(self):
    time.sleep(2) # generation of report
    print("\nSuccessfully generated report and sent to your mobile number ", self.mobile)

#creating second child class of (Book) for cancellation of bookings
class Cancel(Book):
  def cancel(self):
    print("Cancellation of ticket")
    cancelID=int(input("Booking ID: "))
    cancelThread=threading.Thread(target=self.cancelBook, args=(cancelID,)) 
    # creating thread for simultaneously working on cancellation of tickets
    cancelThread.start()
    cancelThread.join()

  def cancelBook(self, cancelID):
    tempFile="tempstore_data.txt" 
    # creating a temporary file to store original data after cancellation or any updates
    with open(FILENAME, "r") as file, open(tempFile, "w") as temp:
      for line in file:
        if line.strip().startswith(str(cancelID)):
          print("Booking cancelled: ", line.strip())
        else:
          temp.write(line)
    os.replace(tempFile, FILENAME)
    print("Successfully cancelled your booking!")

# objects for child class to access function calls       
objPay=Pay()
objCancel=Cancel()

if __name__=="__main__":
  info()
  menu()