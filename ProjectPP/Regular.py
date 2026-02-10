import re
import time
import threading

# Define ANSI escape codes for color and style
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    GOLD = '\033[93m'
    RESET = '\033[0m'

# Function to validate name
def validate_name(name):
    pattern = r'^[A-Za-z\s]{1,50}$'
    return re.match(pattern, name)

# Function to validate phone number
def validate_phone(phone):
    pattern = r'^[6-9]\d{9}$'
    return re.match(pattern, phone)

# Function to validate email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

# Function to validate password
def validate_password(password):
    pattern = r'^.(?=.{8,})(?=.\d)(?=.[a-z])(?=.[A-Z])(?=.[@#$%^&+=]).$'
    return re.match(pattern, password)

# Function to validate confirm password
def validate_confirm_password(password, confirm_password):
    return password == confirm_password

# Function to validate driving license
def validate_driving_license(license):
    pattern = r'^[A-Z]{2}[0-9]{13}$'
    return re.match(pattern, license)

# Introduction and prompt to continue
print(Color.GOLD + " ' ' ' We are presenting a registration form validation in Python, using the example of Car Rental Services' ' ' " + Color.RESET)
print(Color.GOLD + "\nThe script imports various modules, primarily the 're' module for regular expressions." + Color.RESET)

while True:
    choice = input("Press 2 to continue to Registration form: ")
    if choice == '2':
        break
    else:
        print(Color.RED + "Invalid input. Please press 2 to continue." + Color.RESET)

# Registration form
print(Color.GOLD + "\nWelcome to the Car Rental Services!" + Color.RESET)
print(Color.BLUE + "\nEnter the details to complete registration." + Color.RESET)
print(Color.BLUE + "Please enter your name." + Color.RESET)

while True:
    name = input("Name: ")
    if validate_name(name):
        print(Color.GREEN + "Name is valid." + Color.RESET)
        break
    else:
        print(Color.RED + "Please enter a valid name." + Color.RESET)

# Validation for phone number
print(Color.BLUE + "\nPlease enter your phone number." + Color.RESET)
while True:
    phone = input("Phone: ")
    if validate_phone(phone):
        print(Color.GREEN + "Phone number is valid." + Color.RESET)
        break
    else:
        print(Color.RED + "Please enter a valid phone number." + Color.RESET)

# Validation for email
print(Color.BLUE + "\nPlease enter your email." + Color.RESET)
while True:
    email = input("Email: ")
    if validate_email(email):
        print(Color.GREEN + "Email is valid." + Color.RESET)
        break
    else:
        print(Color.RED + "Please enter a valid email address in the format 'example@example.com'." + Color.RESET)

# Validation for password
print(Color.BLUE + "\nPlease enter your password." + Color.RESET)
while True:
    password = input("Password: ")
    if validate_password(password):
        print(Color.GREEN + "Password is valid." + Color.RESET)
        break
    else:
        print(Color.RED + "Please enter a valid password. It must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character." + Color.RESET)

# Validation for confirming password
print(Color.BLUE + "\nPlease confirm your password." + Color.RESET)
while True:
    confirm_password = input("Confirm Password: ")
    if validate_confirm_password(password, confirm_password):
        print(Color.GREEN + "Passwords match." + Color.RESET)
        break
    else:
        print(Color.RED + "Passwords do not match." + Color.RESET)

# Registration successful message
print(Color.GREEN + f"\nAll inputs are valid. \nRegistration successful! \nWelcome to Car Rental Services, {name}!" + Color.RESET)

# Offer car rental option
while True:
    rent_car = input("Would you like to rent a car? (yes/no): ").lower()
    if rent_car == 'yes':
        break
    elif rent_car == 'no':
        print("\nThank you for considering Car Rental Services. Have a great day!")
        exit()  # Exiting the program
    else:
        print(Color.RED + "Invalid input. Please enter 'yes' or 'no'." + Color.RESET)

# Car rental service functionality
class Details:
    def _init_(self):
        self.name = ''
        self.address = ''
        self.mobilenumber = ''
        self.drivinglicense = ''
        self.password = ''
        self.rented_cars = []

    def verify_password(self):
        while True:
            password_attempt = input("Enter your password to proceed with payment: ")
            if password_attempt == self.password:
                print(Color.GREEN + "Password verified." + Color.RESET)
                break
            else:
                print(Color.RED + "Incorrect password. Please try again." + Color.RESET)

    def payMenu(self):
        print("\n1. PhonePe, GPay\n2. UPI\n3. Net Banking\n4. Credit Card\n5. Debit Card\n")

    def payment(self):
        self.verify_password()
        self.payMenu()
        choice = int(input("Select payment method: "))
        if choice in range(1, 6):
            payment_thread = threading.Thread(target=self.payProcessing)
            payment_thread.start()
            payment_thread.join()
            self.genReceipt()
            print(Color.GREEN + f"Thank you {self.name} for choosing Car Rental Services!" + Color.RESET)
        else:
            print("Invalid payment method. Please try again.")
            self.payMenu()
            self.payment()

    def payProcessing(self):
        print("\nPayment Processing..")
        time.sleep(3)  # Processing of payment
        print("Payment Successful..!\n")

    def genReceipt(self):
        time.sleep(2)  # Generation of receipt
        send_to_registered = input("Do you want to send the receipt to your registered number? (yes/no): ").strip().lower()
        if send_to_registered == 'yes':
            print(f"\nSuccessfully generated receipt and sent to your registered mobile number: {self.mobilenumber}")
        else:
            new_number = input("Enter the number to send the receipt: ")
            if validate_phone(new_number):
                print(f"\nSuccessfully generated receipt and sent to the number: {new_number}")
            else:
                print(Color.RED + "Invalid phone number. Receipt not sent." + Color.RESET)

    def check_availability(self):
        print("\nChecking car availability...")
        time.sleep(3)  # Simulate availability
        print("\nCar is available.")

    def add_rental(self, car_name, amount, basis):
        self.rented_cars.append({"car_name": car_name, "amount": amount, "basis": basis})

    def show_rentals(self):
        print(Color.GOLD + "\nDetails of rented cars:" + Color.RESET)
        for i, car in enumerate(self.rented_cars, 1):
            print(f"{i}. Car: {car['car_name']}, Amount: {car['amount']}, Basis: {car['basis']}")

def main():
    carh_rates = [150, 200, 350, 400, 500]
    card_rates = [2000, 2500, 3000, 3750, 4000]
    car_names = ["Tata Punch", "Tata Nexon", "Verna", "Thar", "Fortuner"]
    
    age = int(input("Enter your age: "))
    
    if age > 60:
        print("Due to our car rental policy, individuals above the age of 60 are not eligible to rent a car.")
        return
    elif age < 18:
        print("You are a minor so you cannot drive the car.")
        return
    
    s1 = Details()
    s1.name = name  # Use the name from the registration process
    s1.address = input("\nEnter address: ")
    s1.mobilenumber = phone  # Use the phone from the registration process
    s1.password = password  # Use the password from the registration process
    
    while True:
        s1.drivinglicense = input("Enter driving license: ")
        if validate_driving_license(s1.drivinglicense):
            print(Color.GREEN + "Driving license is valid." + Color.RESET)
            break
        else:
            print(Color.RED + "Please enter a valid driving license (e.g., AB1234567890123)." + Color.RESET)

    total_amount = 0
    
    while True:
        print("\nSelect the following:")
        print("1. Hourly based")
        print("2. Daily based")
        print("3. Exit")
        select = int(input("Enter the choice: "))
        
        if select == 3:
            if total_amount > 0:
                s1.show_rentals()
                print(f"\nThe total amount for all rentals = {total_amount}")
                s1.payment()
            else:
                print("Thanks for visiting")
            break
        
        if select in [1, 2]:
            print("\nSelect the following:")
            print("1. Tata Punch")
            print("2. Tata Nexon")
            print("3. Verna")
            print("4. Thar")
            print("5. Fortuner")
            choice = int(input("Enter the choice: "))
            
            if choice not in range(1, 6):
                print(Color.RED + "Invalid choice. Please try again." + Color.RESET)
                continue
            
            car_name = car_names[choice - 1]
            if select == 1:
                amount = carh_rates[choice - 1]
                basis = 'hours'
            elif select == 2:
                amount = card_rates[choice - 1]
                basis = 'days'
                
            # Ask for duration
            duration = int(input(f"How many {basis} do you want to rent {car_name} for? "))
            total_amount += amount * duration
            s1.check_availability()
            s1.add_rental(car_name, amount * duration, basis)
            print(Color.GREEN + f"{car_name} added to your rental list for {duration} {basis} at a rate of {amount} each {basis}." + Color.RESET)

            # Ask if user wants to rent another car
            another_car = input("Do you want to rent another car? (yes/no): ").lower()
            if another_car == 'no':
                if total_amount > 0:
                    s1.show_rentals()
                    print(f"\nThe total amount for all rentals = {total_amount}")
                    s1.payment()
                else:
                    print("Thanks for visiting")
                break

if __name__ == "__main__":
    main()