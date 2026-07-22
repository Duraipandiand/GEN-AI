'''1. ATM Machine  
Concepts: Function, if-else, while loop  
Ask the user to enter an ATM PIN. 
Allow only 3 attempts. 
If the PIN is correct, display a menu: 
Check Balance 
Deposit Money 
Withdraw Money 
Exit 
If the PIN is incorrect 3 times, lock the account. 
'''
'''
correct_pin = "1234"
balance = 10000



def check_balance():
    print("\nYour Current Balance is: ₹", balance)



def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))
    if amount > 0:
        balance += amount
        print("₹", amount, "deposited successfully.")
        print("Available Balance: ₹", balance)
    else:
        print("Invalid amount!")


def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= 0:
        print("Invalid amount!")

    elif amount > balance:
        print("Insufficient Balance!")

    else:
        balance -= amount
        print("Please collect your cash.")
        print("Available Balance: ₹", balance)


def atm_menu():
    while True:
        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("\nThank you for using our ATM.")
            break

        else:
            print("Invalid Choice! Please try again.")


attempt = 0

while attempt < 3:
    pin = input("Enter ATM PIN: ")

    if pin == correct_pin:
        print("\nLogin Successful!")
        atm_menu()
        break

    else:
        attempt += 1
        print("Incorrect PIN!")

        if attempt < 3:
            print("Remaining Attempts:", 3 - attempt)

if attempt == 3:
    print("\nYour account has been locked.")

'''

'''
2. Online Shopping System  
Concepts: Function, if-elif-else  
Display product categories. 
Ask the user to choose a category. 
Calculate the total bill. 
Apply:
 20% discount if bill > ₹5000 
 10% discount if bill > ₹2000 
 No discount otherwise. 
'''
'''
def category():
    print("welcome to Online shopping ,Please choose below category item to purchase:")
    print("1.Mobile phone and accessories")
    print("2.Dress")
    print("3.Groceries item")
    print()

category()

user_category=int(input("Please select above category:"))

print(f"User selected category is {user_category}")

price=0

def mobile():
    print("Mobile List:\n 1.Samsung s23 ultra price:1,00,000.\n2.Redmi note 12 pro price:40,000.\n3.Iphone 17 price :1,50,000\n")
    print("Please order your mobile model from the listed item.\n")
    model=input()
    if model == 'samsung':
        print("you selected samsung s23 ultra mobile\n")
        price=100000
    elif model == 'redmi':
        print("you selected Redmi note 12 pro mobile\n")
        price=40000
    elif model == 'Iphone':
        print("you selected Iphone 17 mobile\n")
        price=150000
    return price

def Dress():
    print("Dress List:\n 1.Shirt & pant price:1,500.\n2.shirt & dhoti price:2,000.\n3.Saree price :4000\n")
    print("Please order your dress from the listed item.\n")
    model=int(input())
    if model == 1:
        print("you selected Shirts & pant\n")
        price=1500
    elif model == 2:
        print("you selected shirt & dhoti\n")
        price=2000
    elif model == 3:
        print("you selected Saree\n")
        price=4000
    return price

def Grocery():
    print("Grocery List:\n 1.Rice price:1000.\n2.spices price:1,500.\n3.Oil price :400\n")
    print("Please order your grocery from the listed item.\n")
    model=int(input())
    if model == 1:
        print("you selected Rice\n")
        price=1000
    elif model == 2:
        print("you selected spices\n")
        price=1500
    elif model == 3:
        print("you selected oil\n")
        price=400
    return price

match(user_category):
    case 1:
        print("You selected Mobile and accessories:")
        price=mobile()
        print("price amount :",price)
    case 2:
        print("You selected Dress")
        price=Dress()
        print("price amount :",price)
    case 3:
        print("You selected Grocery")
        price=Grocery()
        print("price amount :",price)


if price >5000:
    print("Your eligible for 20% discount for your order.Your total amount:",price)
    print("Bill to pay :",price-(price*.2))
elif price >2000:
    print("Your eligible for 10% discount for your order.Your total amount:",price)
    print("Bill to pay :",price-(price*.1))
else:
    print("bill to pay:",price)

print()

'''

'''
3. Student Grade Calculator  
Concepts: Function, if-elif-else  
Enter marks for 5 subjects. 
Calculate total and average. 
Display grade: 
A 
B 
C 
D 
Fail 
'''

'''
marks= []

for i in range(5):
    value=int(input("please enter marks:"))
    marks.append(value)

print(marks)



def total(marks):
    total_sum=sum(marks)
    print(f"Total marks :{total_sum}")

total(marks)

def average_marks(marks):
    avg=sum(marks)/5
    print(f"Average marks is:{avg}")

average_marks(marks)

if sum(marks)/5 >90:
    print("A grade")
elif sum(marks)/5 >80:
    print("B grade")
elif sum(marks)/5 >70:
    print("C grade")
elif sum(marks)/5 >40:
    print("D grade")
else:
    print("Fail")
    
'''

'''
4. Hospital Appointment Booking  
Concepts: Function, if-else  
Ask whether the patient is new or existing. 
Book appointment. 
Display consultation fee. 
Confirm booking. 
'''
'''
def consultation_fee(patient_type):
    if patient_type == "new":
        return 500
    else:
        return 300


def book_appointment():
    print("===== Hospital Appointment Booking =====")

    name = input("Enter Patient Name: ")
    patient_type = input("Are you a New or Existing patient? ").lower()

    if patient_type == "new":
        print("\nWelcome! You are registered as a NEW patient.")
    elif patient_type == "existing":
        print("\nWelcome back! You are an EXISTING patient.")
    else:
        print("\nInvalid patient type!")
        return

    doctor = input("Enter Doctor Name: ")
    date = input("Enter Appointment Date (DD-MM-YYYY): ")
    time = input("Enter Appointment Time (HH:MM): ")

    fee = consultation_fee(patient_type)

    print("\n------ Appointment Details ------")
    print("Patient Name     :", name)
    print("Patient Type     :", patient_type.title())
    print("Doctor           :", doctor)
    print("Appointment Date :", date)
    print("Appointment Time :", time)
    print("Consultation Fee : ₹", fee)

    confirm = input("\nConfirm booking? (yes/no): ").lower()

    if confirm == "yes":
        print("\n Appointment booked successfully!")
    else:
        print("\n Appointment cancelled.")


book_appointment()
'''


'''
5. Railway Ticket Booking  
Concepts: Function, if-elif-else  
Enter age. 
Apply ticket price: 
Child 
Adult 
Senior Citizen 
Display final ticket amount. 
'''
'''

def railway_ticket():
    age = int(input("Enter passenger age: "))

    if age < 5:
        category = "Child"
        price = 0
    elif age <= 17:
        category = "Child"
        price = 100
    elif age <= 59:
        category = "Adult"
        price = 250
    else:
        category = "Senior Citizen"
        price = 150

    print("\n------ Ticket Details ------")
    print("Passenger Category :", category)
    print("Ticket Price       : ₹", price)


railway_ticket()
'''

'''
6. Employee Salary Calculator  
Concepts: Function, if-elif-else  
Enter basic salary. 
Calculate: 
HRA 
DA 
Bonus 
Display net salary. 
'''

'''

def calculate_salary():
    basic_salary = float(input("Enter Basic Salary: ₹"))

    if basic_salary <= 10000:
        hra = basic_salary * 0.20      
        da = basic_salary * 0.50       
        bonus = 1000

    elif basic_salary <= 30000:
        hra = basic_salary * 0.25      
        da = basic_salary * 0.60       
        bonus = 2000

    else:
        hra = basic_salary * 0.30      
        da = basic_salary * 0.70       
        bonus = 5000

    net_salary = basic_salary + hra + da + bonus

    print("\n------ Salary Slip ------")
    print("Basic Salary : ₹", basic_salary)
    print("HRA          : ₹", hra)
    print("DA           : ₹", da)
    print("Bonus        : ₹", bonus)
    print("--------------------------")
    print("Net Salary   : ₹", net_salary)

calculate_salary()
'''

'''
7. Library Management  
Concepts: Function, if-else  
Search a book. 
If available: 
Issue the book. 
Else: 
Display "Book Not Available." 
'''
'''
books=['science','social','maths','tamil','english']

user_book=input("please enter a book:")

print(user_book)

def search_book(user_book):
    if user_book in books:
        print("Issue the book")
    else:
        print("Book Not avaiable.")

search_book(user_book)

print()
'''

'''
8. Restaurant Billing  
Concepts: Function, for loop  
Customer orders multiple food items. 
Calculate total bill. 
Apply GST. 
Print final invoice. 
'''

'''

def restaurant_bill():
    total = 0

    n = int(input("Enter the number of food items: "))

    for i in range(1, n + 1):
        print(f"\nItem {i}")
        item = input("Enter food item name: ")
        price = float(input("Enter item price: ₹"))

        total = total + price

    gst = total * 0.05      
    final_bill = total + gst

    print("\n========== RESTAURANT INVOICE ==========")
    print("Total Amount : ₹", total)
    print("GST (5%)     : ₹", gst)
    print("----------------------------------------")
    print("Final Bill   : ₹", final_bill)
    print("========================================")

restaurant_bill()
'''


'''
9. Attendance System  
Concepts: Function, for loop  
Enter attendance for 10 students. 
Count: 
Present 
Absent 
Display attendance percentage. 
'''
'''

def attendance_system():
    present = 0
    absent = 0

    for i in range(1, 11):
        attendance = input(f"Enter attendance for Student {i} (P/A): ").upper()

        if attendance == "P":
            present += 1
        elif attendance == "A":
            absent += 1
        else:
            print("Invalid input! Counted as Absent.")
            absent += 1

    attendance_percentage = (present / 10) * 100

    print("\n------ Attendance Report ------")
    print("Total Students      :", 10)
    print("Present Students    :", present)
    print("Absent Students     :", absent)
    print("Attendance Percentage:", attendance_percentage, "%")


attendance_system()
'''

'''
10. Bus Seat Reservation  
Concepts: Function, while loop  
Show available seats. 
Book seats until full. 
Stop booking when no seats remain. 
'''
'''

def reserve_seat():
    total_seats = 5

    while total_seats > 0:
        print("\nAvailable Seats:", total_seats)

        choice = input("Do you want to book a seat? (Y/N): ").upper()

        if choice == "Y":
            total_seats -= 1
            print("Seat booked successfully!")
        elif choice == "N":
            print("Thank you! Visit again.")
            break
        else:
            print("Invalid Choice!")

    if total_seats == 0:
        print("\nSorry! No seats available.")
        print("Bus is FULL.")


reserve_seat()
'''



'''
11. Grocery Store Billing  
Concepts: Function, for loop  
Enter 5 products. 
Enter quantity and price. 
Calculate total bill. 
'''

'''

def grocery_bill():
    total_bill = 0

    print("------ Grocery Store Billing ------")

    for i in range(1, 6):
        print(f"\nProduct {i}")

        product = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price per Item: ₹"))

        amount = quantity * price
        total_bill += amount

        print("Amount = ₹", amount)

    print("\n========== BILL ==========")
    print("Total Bill = ₹", total_bill)
    print("==========================")


grocery_bill()
'''


'''
12. Banking System  
Concepts: Function, while loop, if-elif  
Menu:  
Deposit 
Withdraw 
Check Balance 
Exit  
Repeat until the user chooses Exit. 
'''

'''

def banking_system():
    balance = 1000

    while True:
        print("\n====== BANK MENU ======")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter deposit amount: ₹"))
            balance += amount
            print("Amount deposited successfully.")
            print("Current Balance: ₹", balance)

        elif choice == 2:
            amount = float(input("Enter withdrawal amount: ₹"))

            if amount <= balance:
                balance -= amount
                print("Withdrawal successful.")
                print("Current Balance: ₹", balance)
            else:
                print("Insufficient Balance!")

        elif choice == 3:
            print("Current Balance: ₹", balance)

        elif choice == 4:
            print("Thank you for banking with us!")
            break

        else:
            print("Invalid Choice! Please try again.")


banking_system()
'''

'''
13. Mobile Recharge  
Concepts: Function, if-elif  
Recharge plans:  
₹199 
₹299 
₹399 
₹599
  Display benefits based on the selected plan. 
'''
'''
def menu_display():
    print("Please select below recharge plan:")
    print("1. $199")
    print("2. $299")
    print("3. $399")
    print("4. $599")

menu_display()
user_input=int(input("Please enter recharge plan number:"))

def one_month_plan():
    print("You selected one month recharge plan of $199. \n You have one month incoming and outgoing calls .\n You have 1GB data per day for a month. ")


def Two_month_plan():
    print("You selected two month recharge plan of $299. \n You have one month incoming and outgoing calls .\n You have 1.5GB data per day for a month. ")


def Three_month_plan():
    print("You selected one month recharge plan of $399. \n You have one month incoming and outgoing calls .\n You have 2GB data per day for a month. ")


def Four_month_plan():
    print("You selected one month recharge plan of $599. \n You have one month incoming and outgoing calls .\n You have 2.5GB data per day for a month. ")



if user_input == 1:
    print("You selected $199 monthly plan")
    one_month_plan()
elif user_input == 2:
    print("You selected $299 monthly plan")
    Two_month_plan()
elif user_input == 3:
    print("You selected 3199 monthly plan")
    Three_month_plan()
elif user_input == 4:
    print("You selected $599 monthly plan")
    Four_month_plan()
else:
    print("You selected wrong option.Exit")

print()
print()
print()
'''


'''
14. Cab Booking  
Concepts: Function, if-else  
Ask pickup location. 
Ask destination. 
Calculate fare. 
Confirm booking. 
'''

'''

def cab_booking():
    pickup = input("Enter Pickup Location: ")
    destination = input("Enter Destination: ")
    distance = float(input("Enter Distance (in km): "))

    fare_per_km = 15
    fare = distance * fare_per_km

    print("\nPickup Location :", pickup)
    print("Destination     :", destination)
    print("Distance        :", distance, "km")
    print("Fare            : ₹", fare)

    confirm = input("\nConfirm Booking? (Y/N): ").upper()

    if confirm == "Y":
        print("Cab Booked Successfully!")
        print("Driver will arrive shortly.")
    else:
        print("Booking Cancelled.")


cab_booking()
'''

'''
15. Hotel Room Booking  
Concepts: Function, if-elif  
Room types:  
Standard 
Deluxe 
Suite  
Calculate total amount based on the number of days. 
'''
'''
def room_type():
    print("Please select Room type:\n 1.Standard \n 2.Deluxe \n 3.Suite \n")

room_type()

room=int(input("Please choose which type of room you want:"))

def standard(s):
    print("Standard room cost per day is RS.800")
    print(f"You stayed {a}days in standard room .Total amount is:",s*800)

def deluxe(d):
    print("Deluxe room cost per day is RS.1500")
    print(f"You stayed {d}days in deluxe room .Total amount is:",d*1500)

def suite(su):
    print("suite room cost per day is RS.2500")
    print(f"You stayed {su}days in suite room .Total amount is:",su*2500)

if room == 1:
    print("You selected Standard room type\n")
    standard_days=int(input("Please enter number of days you want to stay:"))
    standard(standard_days)
elif room == 2:
    print("You selected Deluxe room type\n")
    deluxe_days=int(input("Please enter number of days you want to stay:"))
    deluxe(deluxe_days)
elif room == 3:
    print("You selected Suite room type\n")
    suite_days=int(input("Please enter number of days you want to stay:"))
    suite(suite_days)
else:
    print("You selected wrong option.Exit")


print()
print()
print()

'''


'''
16. Movie Ticket Booking
  Concepts: Function, if-else
  Ask movie name.
 Ask number of tickets.
 Calculate bill.
 Confirm booking. 

'''

'''

def movie_booking():
    movie_name = input("Enter Movie Name: ")
    tickets = int(input("Enter Number of Tickets: "))

    ticket_price = 200
    total_bill = tickets * ticket_price

    print("\n====== MOVIE TICKET ======")
    print("Movie Name      :", movie_name)
    print("Number of Tickets:", tickets)
    print("Ticket Price    : ₹", ticket_price)
    print("Total Bill      : ₹", total_bill)

    confirm = input("\nConfirm Booking (Y/N): ").upper()

    if confirm == "Y":
        print("Booking Confirmed!")
        print("Enjoy Your Movie!")
    else:
        print("Booking Cancelled!")


movie_booking()
'''

'''17. Electricity Bill Calculator
  Concepts: Function, if-elif  
  Calculate bill using slabs:  
  0–100 units 
  101–300 units 
  Above 300 units 
'''
'''
electricity_unit=int(input("Please enter units:"))

def calculate_bill(electricity_unit):
    if electricity_unit >= 0 and electricity_unit <=100:
        print(f"Your electricity consumed unit is {electricity_unit} under 0-100 slab per unit cost 5")
        print(f"Total amount is :{electricity_unit*5}")
    elif electricity_unit >= 101 and electricity_unit <=300:
        print(f"Your electricity consumed unit is {electricity_unit} under 101-300 slab per unit cost 10")
        print(f"Total amount is :{electricity_unit*5}")
    elif electricity_unit > 300:
        print(f"Your electricity consumed unit is {electricity_unit} under 300 slab per unit cost 15")
        print(f"Total amount is :{electricity_unit*5}")

calculate_bill(electricity_unit)
print()

'''

'''
18. Password Verification
  Concepts: Function, while loop
  User gets 3 attempts.
 Correct password → Login successful.
 Wrong password → Account locked. 
'''

'''

def verify_password():
    correct_password = "python123"
    attempts = 3

    while attempts > 0:
        password = input("Enter Password: ")

        if password == correct_password:
            print("Login Successful!")
            break
        else:
            attempts -= 1
            print("Wrong Password!")
            print("Attempts Left:", attempts)

    if attempts == 0:
        print("Account Locked!")


verify_password()
'''



'''
19. Online Exam System
  Concepts: Function, for loop
  Ask 10 questions.
 Count correct answers.
 Display score and result. 
'''

'''

def online_exam():
    questions = [
        ("1. What is the capital of India? ", "Delhi"),
        ("2. What is 5 + 3? ", "8"),
        ("3. Which language is used for AI? ", "Python"),
        ("4. What is the national animal of India? ", "Tiger"),
        ("5. What is the largest planet? ", "Jupiter"),
        ("6. What is 10 x 2? ", "20"),
        ("7. Which is the fastest land animal? ", "Cheetah"),
        ("8. What is the color of the sky? ", "Blue"),
        ("9. How many days are there in a week? ", "7"),
        ("10. What is the chemical symbol of water? ", "H2O")
    ]

    score = 0

    for question, answer in questions:
        user_answer = input(question)

        if user_answer.lower() == answer.lower():
            score += 1

    print("\n====== EXAM RESULT ======")
    print("Correct Answers :", score)
    print("Wrong Answers   :", 10 - score)
    print("Score           :", score, "/10")

    if score >= 5:
        print("Result : PASS")
    else:
        print("Result : FAIL")


online_exam()
'''

'''
20. Vehicle Parking System
  Concepts: Function, while loop
  Menu:
  Park Vehicle
 Remove Vehicle
 View Available Slots
 Exit 
'''

'''

def parking_system():
    available_slots = 5

    while True:
        print("\n====== VEHICLE PARKING SYSTEM ======")
        print("1. Park Vehicle")
        print("2. Remove Vehicle")
        print("3. View Available Slots")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            if available_slots > 0:
                vehicle = input("Enter Vehicle Number: ")
                available_slots -= 1
                print(vehicle, "parked successfully.")
            else:
                print("Parking Full!")

        elif choice == 2:
            vehicle = input("Enter Vehicle Number: ")
            if available_slots < 5:
                available_slots += 1
                print(vehicle, "removed successfully.")
            else:
                print("Parking is already empty.")

        elif choice == 3:
            print("Available Slots:", available_slots)

        elif choice == 4:
            print("Thank You!")
            break

        else:
  
            print("Invalid Choice!")


parking_system()

'''

'''
21. Inventory Management
  Concepts: Function, for loop
  Store products.
 Display low-stock products (quantity less than 10).
 Calculate total inventory value. 
'''
'''

def inventory_management():
    total_value = 0

    print("------ Inventory Management ------")

    for i in range(1, 6):
        print(f"\nProduct {i}")

        product = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price per Item: ₹"))

        value = quantity * price
        total_value += value

        if quantity < 10:
            print(product, "-> Low Stock")

    print("\n====== INVENTORY REPORT ======")
    print("Total Inventory Value : ₹", total_value)


inventory_management()
'''


'''
22. Employee Attendance System
  Concepts: Function, for loop, if-else
  Enter attendance for employees.
 Count present and absent employees.
 Display attendance report. 
'''
'''

def employee_attendance():
    present = 0
    absent = 0

    for i in range(1, 6):
        print(f"\nEmployee {i}")
        name = input("Enter Employee Name: ")
        attendance = input("Enter Attendance (P/A): ").upper()

        if attendance == "P":
            present += 1
        elif attendance == "A":
            absent += 1
        else:
            print("Invalid Input! Counted as Absent.")
            absent += 1

    print("\n====== ATTENDANCE REPORT ======")
    print("Total Employees :", present + absent)
    print("Present         :", present)
    print("Absent          :", absent)


employee_attendance()
'''

'''23. Flight Ticket Booking
  Concepts: Function, if-elif
 Choose class:
    Economy
    Business
     First Class 
Calculate total ticket fare. 
'''
'''
def categories():
    print("choose Class:")
    print("Economy")
    print("Business")
    print("First Class")

categories()

class_type=input("please enter a class type:")
number_tickets=int(input("Please enter a ticket count:"))

def flight_ticket_fare(class_type,number_tickets):
    if class_type == 'Economy':
        print(f"You selected {class_type} categories price is 7000")
        print(f"Total ticket fare is:{7000*number_tickets}")
    elif class_type == 'Business':
        print(f"You selected {class_type} categories price is 12000")
        print(f"Total ticket fare is:{12000*number_tickets}")
    elif class_type == 'First Class':
        print(f"You selected {class_type} categories price is 20000")
        print(f"Total ticket fare is:{20000*number_tickets}")

flight_ticket_fare(class_type,number_tickets)
'''


'''
24. E-Commerce Order Tracking
  Concepts: Function, if-elif
  Display order status:
  Ordered
 Packed
 Shipped
 Out for Delivery
 Delivered 
'''
'''


def order_tracking():
    print("Order Status")
    print("1. Ordered")
    print("2. Packed")
    print("3. Shipped")
    print("4. Out for Delivery")
    print("5. Delivered")

    status = int(input("Enter Order Status (1-5): "))

    print("\n====== ORDER TRACKING ======")

    if status == 1:
        print("Status : Ordered")
        print("Your order has been placed successfully.")

    elif status == 2:
        print("Status : Packed")
        print("Your order has been packed.")

    elif status == 3:
        print("Status : Shipped")
        print("Your order has been shipped.")

    elif status == 4:
        print("Status : Out for Delivery")
        print("Your order is on the way.")

    elif status == 5:
        print("Status : Delivered")
        print("Your order has been delivered successfully.")

    else:
        print("Invalid Order Status!")


order_tracking()
'''


'''
25. Hospital Billing System
  Concepts: Function, if-elif
  Calculate:  
  Consultation fee
 Room charges
 Medicine charges
 GST
` Final bill 
'''
'''

def hospital_bill():
    patient_name = input("Enter Patient Name: ")

    print("\nSelect Room Type")
    print("1. General Ward")
    print("2. Semi-Private")
    print("3. Private")

    room = int(input("Enter Room Type (1-3): "))
    days = int(input("Enter Number of Days: "))
    medicine_charges = float(input("Enter Medicine Charges: ₹"))

    consultation_fee = 500

    if room == 1:
        room_charge = days * 1000
    elif room == 2:
        room_charge = days * 2000
    elif room == 3:
        room_charge = days * 3000
    else:
        print("Invalid Room Type!")
        return

    subtotal = consultation_fee + room_charge + medicine_charges
    gst = subtotal * 0.05
    final_bill = subtotal + gst

    print("\n========== HOSPITAL BILL ==========")
    print("Patient Name       :", patient_name)
    print("Consultation Fee   : ₹", consultation_fee)
    print("Room Charges       : ₹", room_charge)
    print("Medicine Charges   : ₹", medicine_charges)
    print("GST (5%)           : ₹", gst)
    print("-----------------------------------")
    print("Final Bill         : ₹", final_bill)


hospital_bill()
'''