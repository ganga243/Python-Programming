# Exercise 1: Traffic Light Simulator
# ---------------------------------------------
# color = input("Enter light color:")

# if color == "red":
#     print("stop")
# elif color == "yellow":
#     print("Slow down")
# elif color == "green":
#     print("Go")
# else:
#     print("Invalid color")

# Exercise 2: Even or Odd
# -----------------------------------
# number = int(input("Enter a whole number:"))

# if number % 2 ==0:
#     print("Even")
# else:
#     print("Odd")

# 1. Positive, Negative or Zero
# -----------------------------------------
# number = int(input("Enter a number:"))

# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print("Zero")

# 2. Eligible to Vote
# ------------------------------------
# age = int(input("Enter your age:"))

# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")

# 3.Temperature Checker
# -----------------------------------
# temperature = int(input("Enter temperature:"))

# if temperature <20:
#     print("Cold")
# elif temperature <= 30:
#     print("Warm")
# else:
#     print("Hot")

# 4.Leap Year
# -------------------------

# year = int(input("Enter a year: "))

# if year % 400 == 0:
#     print("Leap year")
# elif year % 100 == 0:
#     print("Not a leap year")
# elif year % 4 == 0:
#     print("Leap year")
# else:
#     print("Not a leap year")

# 5. Student Grade Calculator
# ----------------------------------------
# marks = int(input("Enter marks:"))

# if marks >= 90:
#     print("Grade A")
# elif marks >= 80:
#     print("Grade B")
# elif marks >= 70:
#     print("Grade C")
# elif marks >= 60:
#     print("Grade D")
# else:
#     print("Grade F")

# 6. Positive and Even
# ---------------------------------------
# number = int(input("Enter a number:"))

# if number > 0 and number % 2 ==0:
#     print("positive and Even")
# else:
#     print("Not positive or not even")

# 7.Largest of Three Numbers
# -----------------------------------

# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# c = int(input("Enter third number:"))

# if a >= b and a >= c:
#     print("Largest number is", a)
# elif b >= a and b >= c:
#     print("Largest number is", b)
# else:
#     print("Largest number is ", c)

# 8.Shop Discount Calculator
# -----------------------------------------


# amount = float(input("Enter purchase amount: "))

# if amount > 5000:
#     discount = amount * 20 / 100
# elif amount >= 2000:
#     discount = amount * 10 / 100
# else:
#     discount = 0

# final_bill = amount - discount

# print("Discount =", discount)
#  print("Final bill =", final_bill)

# 9.Day Number to Weekday
# --------------------------------------

# day = int(input("Enter day number (1-7): "))

# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("Invalid day")

# Part 1: For Loop
# --------------------------------------
# for i in range(1, 11):
#     print(i)

# 2. Multiplication table
# -----------------------------------------

# n = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)

# 3. Sum of numbers from 1 to n
# -----------------------------------------------

# n = int(input("Enter a number: "))
# total = 0

# for i in range(1, n + 1):
#     total = total + i

# print("Sum =", total)

# 4. First n Fibonacci numbers
# -------------------------------------------

# n = int(input("Enter how many numbers: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# 5. Star pattern
# -----------------------------------

# for i in range(1, 5):
#     print("*" * i)

# 6. Reverse a string using a loop
# -------------------------------------------------

# word = input("Enter a word: ")
# reverse = ""

# for i in word:
#     reverse = i + reverse

# print("Reverse =", reverse)

# 7. Even numbers from 1 to 50
# -------------------------------------------

# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)

# Part 2: While Loop
# ----------------------------------------
# 8. Print numbers from n to 1
# -----------------------------------
# n = int(input("Enter a number: "))

# while n >= 1:
#     print(n)
#     n = n - 1

# 9. Factorial using while loop
# ---------------------------------------

# n = int(input("Enter a number: "))
# fact = 1

# while n > 0:
#     fact = fact * n
#     n = n - 1

# print("Factorial =", fact)

# 10. Print all digits separately
# -------------------------------------------

# n = int(input("Enter a number: "))

# if n < 0:
#     n = -n

# if n == 0:
#     print(0)
# else:
#     while n > 0:
#         digit = n % 10
#         print(digit)
#         n = n // 10

# 11. Count the number of digits
# --------------------------------------------

# n = int(input("Enter a number: "))
# n = abs(n)
# count = 0

# if n == 0:
#     count = 1
# else:
#     while n > 0:
#         count = count + 1
#         n = n // 10

# print("Number of digits =", count)

# 12. Take input until the user enters "exit"
# -----------------------------------------------------

# while True:
#     text = input("Enter something (or exit): ")

#     if text == "exit":
#         break

#     print("You entered:", text)

# Part 3: Loop Control Statements
# -----------------------------------
# 13. Use break to stop when a number is found
# ------------------------------------------------------

# numbers = [10, 20, 30, 40, 50]
# target = int(input("Enter number to find: "))

# for i in numbers:
#     if i == target:
#         print("Number found")
#         break
# else:
#     print("Number not found")

# 14. Use continue to skip even numbers
# -----------------------------------------------

# for i in range(1, 21):
#     if i % 2 == 0:
#         continue
#     print(i)

# 15. Use pass inside a loop
# -----------------------------------

# for i in range(1, 6):
#     if i == 3:
#         pass
#     print(i)

# Part 4: Match Statements
# ---------------------------------
# 1. Day classifier

# day = int(input("Enter day number (1-7): "))

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6 | 7:
#         print("Weekend")
#     case _:
#         print("Invalid day")

# 2. Simple calculator
# -----------------------------

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /): ")

# match op:
#     case "+":
#         print("Result =", a + b)
#     case "-":
#         print("Result =", a - b)
#     case "*":
#         print("Result =", a * b)
#     case "/":
#         if b != 0:
#             print("Result =", a / b)
#         else:
#             print("Cannot divide by zero")
#     case _:
#         print("Invalid operator")

# 3. Grade checker using guards
# -----------------------------------------

# marks = int(input("Enter marks (0-100): "))

# match marks:
#     case x if 90 <= x <= 100:
#         print("Grade A")
#     case x if 80 <= x < 90:
#         print("Grade B")
#     case x if 70 <= x < 80:
#         print("Grade C")
#     case x if 60 <= x < 70:
#         print("Grade D")
#     case x if 0 <= x < 60:
#         print("Grade F")
#     case _:
#         print("Invalid marks")

# 4. HTTP status handler
# -----------------------------------

# status = int(input("Enter HTTP status code: "))

# match status:
#     case 200:
#         print("OK")
#     case 404:
#         print("Not Found")
#     case x if 500 <= x <= 599:
#         print("Server Error")
#     case x if 400 <= x <= 499:
#         print("Client Error")
#     case _:
#         print("Other Status")

# 5. Chess board color
# --------------------------------
# row = int(input("Enter row (1-8): "))
# col = int(input("Enter column (1-8): "))

# match (row % 2, col % 2):
#     case (1, 1) | (0, 0):
#         print("White")
#     case (1, 0) | (0, 1):
#         print("Black")
#     case _:
#         print("Invalid position")

# 6. Command parser
# -----------------------------------

# cmd = ["add", 5, 3]

# match cmd:
#     case ["add", a, b]:
#         print("Result =", a + b)
#     case ["quit"]:
#         print("Program stopped")
#     case _:
#         print("Invalid command")

# 7. File type checker
# ------------------------------

# filename = input("Enter filename: ")
# parts = filename.split(".")

# match parts:
#     case [name, "jpg" | "png"]:
#         print("Image file")
#     case [name, "py"]:
#         print("Python file")
#     case _:
#         print("Unknown file type")

# 8. Shape area calculator
# -------------------------------------

# import math

# shape = ("circle", 5)

# match shape:
#     case ("circle", radius):
#         area = math.pi * radius * radius
#         print("Area of circle =", round(area, 2))
#     case ("rect", length, width):
#         area = length * width
#         print("Area of rectangle =", area)
#     case _:
#         print("Invalid shape")







