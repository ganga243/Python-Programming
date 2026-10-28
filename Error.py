# # # 1. NameError - variable not defined
# # # print(x)

# # # 2. TypeError - Invalid type used in an operation
# # # print(1 + '1')

# # # 3. ValueError - Wrong Type
# # # n = int(input("Enter a number"))

# # # 4. IndexError - Index out of range
# # # l1 = [4,5,6]
# # # print(l1[5])

# # # 5. KeyError - dictionary key missing
# # student = {
# #     "name":"Amal"
# # }
# # print(student['name'])

# # # 6. ZeroDivisionError - Division by zero
# # # print(10/0)

#  7. AttributeError - oru object illatha attributr or methode use cheyyan try akunna tymil ulla error
# name = "Jithu"
#  name.append()

#  8.fileNotFoundError - file does not exist
# 9.ImportError - cannot import a module


# Except Handling
# -----------------------

# try :
#     # code that may generate an error
#     pass
# except:
#     # handles the error
#     pass
# else:
#     # excecutes if no errors occur
#     pass
# finally:
#     # excecutes even if error occurs or not
#     pass

try:
    number1 = int(input("Enter a first  number: "))
    number2 = int(input("Enter a second number: "))
    count = int(input("Enter a count: "))
    result = (number1 + number2)/count

except ZeroDivisionError:
         print("The number should  not be zero.")
except ValueError:
         print("Input must be an integer  value.")
else:
       print(result)
finally:
       print("Operation completed")


# try:
#        number = int(input("Enter a number:"))
#        print(100/number)
# except (ZeroDivisionError,ValueError):
#        print("error occured")
# try:
#     number = int(input("Enter a number: "))
#     print(100/number)
#     print(result)
# except Exception as e:
#     print("Error occured")
# print("After the exception handling block")