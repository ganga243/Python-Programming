#if statement
#if-else statement
#if-elif-else statement
#Nested if

#if condition if
    # block of code
    #   .
    #   .
    #   .
#if condition:
#    if-block
#else
#     else-block

# age = 100
# if age>=18:
#     print('Adult')
# # ------------------------------------- Example of if statement
# if age>=18:
#     print("child")
# print('after if block')
# # ----------------------------------------Example for if-else statement

# if age > 0 and age < 13:   #Exampl efor if -elif -else ststement
#     print('child')
# elif age >= 13 and age <20:
#     print('teenager')
# elif age >= 20 and age <60:
#     print('adult')
# elif age >= 60:
#     print('senior citizen')
# else:
#     print('invalid entry')

# print('-----------')
# ----------------------------------------
# Nested -if--------------------

# age = int(input("Enter your age:"))
# mark = int(input("Enter your mark"))

# if age>= 18:
#     print("Age requriment satisfied...")
#     if mark >= 50:
#         print("Admission approved...")
#     else:
#         print("Admission rejected: insufficient marks")
# else:
#     print("Admission rejected: Age requrirement is not satisfied")

# ---------------------------------------------------------------------------------

# day = int(input("Enter the number of day: "))
# match day:
#     case 1:
#           print('Monday')
#     case 2:
#           print('Tuesday')
#     case 3:
#           print('Wednesday')
#     case 4:
#           print('Thursday')
#     case 5:
#           print('Friday')
#     case _:
#           print('Invalid entry')
# -----------------------------------------------------------
# eg:2
# mark = int(input("Enter the mark: "))
# if mark >90 and mark <=100:
#     print("A+")
# elif mark >80 and mark <=90:
#     print("A")
# elif mark >70 and mark <=80:
#     print("B+")
# elif mark >60 and mark <=70:
#     print("B")
# elif mark >50 and mark <=60:
#     print("C")
# elif mark >40 and mark <=500:
#     print("D")
# elif mark >40 and mark >=0:
#     print("E")
# else:
#     print("Invalid mark entry!!!!!!!!!!!!")

# ------------------------------------------------------------------

day= "monday"

match day.capitalize():
    case "Monday"| "Tuesday"| "Wednesday"| "Thursday"| "Friday":
        print("Weekday")
    case "Sunday" | "Saturday":
        print("Weekend")
    case _:
        print("Invalid")





