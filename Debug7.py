# name = "Rahul"
# age = 20
# print("Name:",name)
# print("Age next year:",age+1)
# ---------------------------------------------
# 2.
# student_name = "Anu"
# student_age = 21
# student_course = "Python"

# print(student_name)
# print(student_age)
# print(student_course)
# --------------------------------------------
# 3.
# price = 99.50
# quantity = 3

# total = price * quantity
# print("Total:",total)
# -----------------------------------------------
# 4.
# x = 10
# y = 20
# total = x + y
# print(total)
# --------------------------------------------------
# 5.
# first_name = "Arun"
# last_name = "Kumar"

# full_name = first_name + "" + last_name
# print("Full name:" + full_name)
# print("Name length:",len(full_name))
# ------------------------------------------------
# 6.Level 2-> Operators
# a = 15
# b = 4

# print("Addition:",a + b)
# print("Subtraction:",a - b)
# print("Multiplication:",a * b)
# print("Division:",a // b)
# print("Remainder:",a % b)
# --------------------------------------
# 7.
# marks = 75

# if marks == 75:
#     print("Marks are 75")
# ------------------------------------------
# 8.
# age = 20
# if age > 18 and age < 25:
#     print("Eligible")
# ----------------------------------------------
# 9.
# a = 10
# b = 20

# result = a > b & a < b

# print("Result:", result)
# ------------------------------------------------
# 10.
# x = 10
# y = 3

# print(x ** y)
# 
# -------------------------------------------------
# 11.Level 3 input & Type conversion
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")
# ------------------------------------------
# 12.
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# total = num1 + num2

# print("Sum:", total)
# ---------------------------------------------
# 13.
# temperature = int(input("Enter temperature: "))

# if temperature > 30:
#     print("Hot")
# else:
#     print("Normal")
# ----------------------------------------------------
# 14.
# radius = float(input("Enter radius: "))

# area = 3.14 * radius * radius

# print("Area:", area)
# -----------------------------------------------
# 15.Level->4 Conditional statements
# marks = 85

# if marks >= 90:
#     print("A")
# elif marks >= 75:
#     print("B")
# elif marks >= 50:
#     print("C")
# else:
#     print("Fail")
# ------------------------------------------------
# 16.
# age = 18
# if age >= 18:
#     print("You can vote")
# else:
#     print("You cannot vote")
# -------------------------------------------------
# 17.
# number = 3

# if number % 2 == 0:
#    print("Even")
# else:
#    print("Odd")
# --------------------------------------------
# 18.
# username = "admin"
# password = "1234"

# if username == "admin":
#     if password == "1234":
#         print("Login successful")
#     else:
#         print("Wrong password")
# else:
#     print("Wrong username")
# -----------------------------------------------

# 19. level->5 if,elif,else
# marks = 95

# if marks >= 90:
#     grade = "A"
# elif marks >= 75:
#     grade = "B"
# elif marks >= 50:
#     grade = "C"
# else:
#     grade = "F"

# print(grade)
# -------------------------------------------------

# 20.
# number = 1

# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# elif number == 0:
#     print("Zero")
# ---------------------------------------------

# 21.
# age = 10

# if age >= 60:
#     print("Senior Citizen")
# elif age >= 18:
#     print("Adult")
# else:
#     print("Minor")
# --------------------------------------
# 22.Level->6 Combined debugging
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# if age >= 18:
#     print(name + " is eligible to vote")
# else:
#     print(name + " is not eligible to vote")
# --------------------------------------------------
# 23.
# price = float(input("Enter product price: "))
# discount = float(input("Enter discount percentage: "))

# discount_amount = price * discount / 100
# final_price = price - discount_amount

# print("Final price:", final_price)
# ------------------------------------------------------
# 24.
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("Even number")
# elif number % 2 == 1:
#     print("Odd number")
# else:
#     print("Invalid")
# -----------------------------------------------------
# 25.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if a > b:
#     print(a, "is greater")
# elif b > a:
#     print(b, "is greater")
# else:
#     print("Both numbers are equal")
# ---------------------------------------------------

# 26. Level->7 Challenge questions
# year = int(input("Enter your birth year: "))
# age = 2026 - year
# print("Your age is:", age)
# --------------------------------------------------
# 27.
# num = 15

# if num % 3 == 0 and num % 5 == 0:
#     print("Divisible by both")
# elif num % 3 == 0:
#     print("Divisible by 3")
# elif num % 5 == 0:
#     print("Divisible by 5")
# else:
#     print("Not divisible by 3 or 5")
# ----------------------------------------------------------
# 28.
# marks = 82
# attendance = 75

# if marks >= 50 and attendance >= 75:
#     print("Eligible for exam")
# else:
#     print("Not eligible")
# ----------------------------------------------------
# a = 10
# b = 40
# c = 30

# if a > b and a > c:
#     largest = a
# elif b > a and b > c:
#     largest = b
# else:
#     largest = c

# print("Largest:", largest)
# random module->26 game print  cheyyan pattunnu indo check chekkannam
# 24.module function check cheyyannam

# 29. Collection + Function
# def calculate_average(marks):
#     total = sum(marks)
#     average = total / len(marks)
#     return average

# marks = [75, 80, 90, 85]

# print("Average:", calculate_average(marks))
# -------------------------------------------------------------

# 30. Function + Dictionary
# def display_student(student):
#     print("Name:", student["name"])
#     print("Age:", student["age"])
#     print("Course:", student.get("course", "Not available"))

# student = {
#     "name": "Arun",
#     "age": 21
# }

# display_student(student)
# -----------------------------------------------------------

# 31.Function + Set
# d
# def count_unique(numbers):
#     unique = set(numbers)
#     return len(unique)

# numbers = [10, 20, 10, 30, 20, 40]

# print("Unique numbers:", count_unique(numbers))
# ------------------------------------------------------------

# 32.Module + Function
# import math
# def calculate_circle_area(radius):
#     return math.pi * radius ** 2

# print(calculate_circle_area(5))
# --------------------------------------------------------

# 33.
# def find_passed_students(marks):
#     passed = []

#     for mark in marks:
#         if mark >= 40:
#             passed.append(mark)

#     return passed

# marks = [35, 40, 45, 60, 72]

# print(find_passed_students(marks))
# -----------------------------------------------------

# 34..
# import math

# def calculate_discount(price, percentage):
#     discount = price * percentage / 100
#     return price - discount

# product = {
#     "name": "Laptop",
#     "price": "50000",
#     "discount": 10
# }

# final_price = calculate_discount(
#     int(product["price"]),
#     product["discount"]
# )

# print("Final price:", math.floor(final_price))
# ---------------------------------------------------------

# 35.
# import random

# def generate_student():
#     student = {
#         "name": "Anu",
#         "marks": [78, 85, 92, 67]
#     }

#     average = sum(student["marks"]) / len(student["marks"])

#     if average >= 90:
#         grade = "A"
#     elif average >= 75:
#         grade = "B"
#     elif average >= 50:
#         grade = "C"
#     else:
#         grade = "F"

#     student["average"] = average
#     student["grade"] = grade
#     student["id"] = random.randint(1000, 9999)

#     return student
# result = generate_student()

# print("Student:", result["name"])
# print("Average:", result["average"])
# print("Grade:", result["grade"])
# print("ID:", result["id"])