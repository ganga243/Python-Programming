# 1. Student Grade Calculator
# -------------------------------------------

# mark = int(input("Enter mark: "))

# if mark >= 90:
#     print("Grade A+")
# elif mark >= 80:
#     print("Grade A")
# elif mark >= 70:
#     print("Grade B")
# elif mark >= 60:
#     print("Grade C")
# elif mark >= 50:
#     print("Grade D")
# else:
#     print("Fail")

# 2. ATM Withdrawal System
# -------------------------------------------

# balance = int(input("Enter account balance: "))
# amount = int(input("Enter withdrawal amount: "))

# if amount > balance:
#     print("Insufficient Balance")
# elif amount % 100 != 0:
#     print("Enter an amount in multiples of 100")
# else:
#     print("Withdrawal Successful")

# 3. Online Shopping Delivery Charge
# -------------------------------------------------

# order = int(input("Enter order value: "))

# if order >= 5000:
#     charge = 0
# elif order >= 2000:
#     charge = 50
# else:
#     charge = 100

# total = order + charge

# print("Delivery charge =", charge)
# print("Final amount =", total)

# . Employee Performance Rating
# ------------------------------------------

# score = int(input("Enter performance score: "))

# if score >= 90:
#     print("Excellent")
# elif score >= 75:
#     print("Very Good")
# elif score >= 60:
#     print("Good")
# elif score >= 40:
#     print("Needs Improvement")
# else:
#     print("Poor")

# 5. Electricity Bill Calculator
# ----------------------------------------

# units = int(input("Enter units: "))

# if units <= 100:
#     bill = units * 2
# elif units <= 200:
#     bill = (100 * 2) + (units - 100) * 3
# elif units <= 400:
#     bill = (100 * 2) + (100 * 3) + (units - 200) * 5
# else:
#     bill = (100 * 2) + (100 * 3) + (200 * 5) + (units - 400) * 7

# print("Electricity bill =", bill)

# 6. Movie Ticket Pricing
# ------------------------------------

# age = int(input("Enter age: "))

# if age < 5:
#     print("Ticket price = Free")
# elif age <= 12:
#     print("Ticket price = ₹100")
# elif age <= 59:
#     print("Ticket price = ₹200")
# else:
#     print("Ticket price = ₹120")

# 7. Traffic Fine System
# ------------------------------------

# speed = int(input("Enter vehicle speed: "))

# if speed <= 60:
#     print("No fine")
# elif speed <= 80:
#     print("Fine = ₹500")
# elif speed <= 100:
#     print("Fine = ₹1000")
# else:
#     print("Fine = ₹2000")
#     print("License Review")

# 8. Restaurant Billing System
# ----------------------------------------------

# bill = float(input("Enter total bill: "))

# if bill >= 5000:
#     discount = bill * 20 / 100
# elif bill >= 3000:
#     discount = bill * 15 / 100
# elif bill >= 1000:
#     discount = bill * 10 / 100
# else:
#     discount = 0

# final_bill = bill - discount

# print("Discount =", discount)
# print("Final bill =", final_bill)

# 9. College Admission Decision
# ------------------------------------------

# score = int(input("Enter entrance score: "))

# if score >= 90:
#     print("Direct Admission")
# elif score >= 75:
#     print("Admission + Interview")
# elif score >= 60:
#     print("Waitlisted")
# else:
#     print("Not Eligible")

# 10. Bank Loan Risk Category
# -----------------------------------------------

# score = int(input("Enter credit score: "))
# default = input("Existing loan default? yes/no: ")

# if default == "yes":
#     print("Loan Approval Requires Manual Review")
# elif score >= 750:
#     print("Low Risk")
# elif score >= 650:
#     print("Medium Risk")
# elif score >= 550:
#     print("High Risk")
# else:
#     print("Very High Risk")

# 11. Hotel Room Pricing
# ----------------------------------------------

# room = input("Enter room type: ").lower()
# nights = int(input("Enter number of nights: "))

# if room == "standard":
#     price = 2000
# elif room == "deluxe":
#     price = 3500
# elif room == "suite":
#     price = 5000
# else:
#     price = 0

# total = price * nights

# if nights > 5:
#     total = total - (total * 10 / 100)

# print("Final bill =", total)

# 12. Employee Bonus Calculator
# -------------------------------------------

# salary = float(input("Enter annual salary: "))
# performance = int(input("Enter performance score: "))

# if performance >= 90:
#     bonus = salary * 20 / 100
# elif performance >= 75:
#     bonus = salary * 15 / 100
# elif performance >= 60:
#     bonus = salary * 10 / 100
# else:
#     bonus = 0

# print("Bonus =", bonus)

# 13. Mobile Data Plan
# ----------------------------------------

# data = float(input("Enter monthly data requirement: "))

# if data < 5:
#     print("Basic Plan - ₹199")
# elif data <= 20:
#     print("Standard Plan - ₹399")
# elif data <= 50:
#     print("Premium Plan - ₹699")
# else:
#     print("Unlimited Plan - ₹999")

# 14. Parking Fee Calculator
# -----------------------------------------

# hours = int(input("Enter parking hours: "))
# electric = input("Is it an electric vehicle? yes/no: ")

# if hours <= 2:
#     fee = 30
# elif hours <= 5:
#     fee = 50
# elif hours <= 10:
#     fee = 100
# else:
#     fee = 150

# if electric == "yes":
#     fee = fee - (fee * 20 / 100)

# print("Final parking fee =", fee)

# 15. Online Exam Result
# ----------------------------------------

# theory = int(input("Enter theory mark: "))
# practical = int(input("Enter practical mark: "))

# if theory < 40 or practical < 40:
#     print("Fail")
# else:
#     average = (theory + practical) / 2

#     if average >= 75:
#         print("Distinction")
#     elif average >= 60:
#         print("First Class")
#     elif average >= 50:
#         print("Second Class")
#     else:
#         print("Pass")

# 16. Flight Baggage Fee
# ----------------------------------------

# weight = float(input("Enter baggage weight: "))
# class_type = input("Enter class: ").lower()

# if class_type == "business":
#     free_limit = 25
# else:
#     free_limit = 15

# if weight <= free_limit:
#     charge = 0
# elif weight <= 20:
#     charge = 500
# elif weight <= 30:
#     charge = 1000
# else:
#     charge = 2000

# print("Baggage charge =", charge)

# E-Commerce Return Eligibility
# -------------------------------------------------

# days = int(input("Enter days since purchase: "))
# unused = input("Product unused? yes/no: ")
# returnable = input("Product returnable? yes/no: ")

# if days <= 7 and unused == "yes" and returnable == "yes":
#     print("Return Approved")
# else:
#     if days > 7:
#         print("Return Rejected - Purchased more than 7 days ago")
#     elif unused != "yes":
#         print("Return Rejected - Product is used")
#     else:
#         print("Return Rejected - Product is not returnable")

# 18 Salary Tax Calculation
# ------------------------------------------

# salary = float(input("Enter salary: "))

# if salary <= 300000:
#     tax = 0
# elif salary <= 600000:
#     tax = salary * 5 / 100
# elif salary <= 1000000:
#     tax = salary * 10 / 100
# else:
#     tax = salary * 20 / 100

# final_salary = salary - tax

# print("Tax =", tax)
# print("Final Salary =", final_salary)

# 19 Ride Fare Calculation
# ---------------------------------------

# distance = float(input("Enter distance in km: "))
# peak = input("Is it peak hour? ").lower()

# if distance <= 5:
#     fare = 100
# elif distance <= 15:
#     fare = 100 + (distance - 5) * 15
# elif distance <= 30:
#     fare = 100 + (10 * 15) + (distance - 15) * 12
# else:
#     fare = 100 + (10 * 15) + (15 * 12) + (distance - 30) * 10

# if peak == "yes":
#     fare = fare + (fare * 20 / 100)

# print("Total Fare =", fare)

# 20 Employee Leave Approval
# -----------------------------------------

requested = int(input("Enter requested leave days: "))
available = int(input("Enter available leave days: "))

if requested > available:
    print("Leave Rejected")
elif requested <= 3:
    print("Leave Automatically Approved")
elif requested <= 7:
    print("Manager Approval Required")
else:
    print("HR Approval Required")