16/10/26
# -------
# sum 
# ---

# n = int(input("Enter a multi-digit number: "))
# sum = 0
# while n > 0:
    # r = n % 10
    # sum += r
    # n //= 10
# else:
    # print(f"Sum is {sum}") 


# Reverse of a number
# --------------------

# n = int(input("Enter a multi-digit number: "))

# rev = 0
# while n > 0:
#     r = n % 10
#     rev = (rev * 10) + r
#     n //= 10
# else:
#     print("Reverse is", rev)


# PALINDROME OR NOT
# ------------------

# n = int(input("Enter a multi-digit number: "))

# run = n

# rev = 0
# while n > 0:
#     r = n % 10
#     rev = (rev * 10) + r
#     n //= 10
# else:
#     print("Reverse is", rev)

# palindrome_or_not = "Palindrome" if run == rev else "Not a Palindrome"

# print(palindrome_or_not)


# LIST COMPREHENSION(even)
# ------------------

# l2 = [45, 86, 97, 41, 37, 54, 28, 36]

# even_numbers = []

# for x in l2:
#     if x % 2 == 0:
#         even_numbers.append(x)

# print(even_numbers)


# List comprehension(squared)
# --------------------------

# l1 = [45, 86, 97, 41, 37, 54, 28, 36]

# new_list = [x for x in l1]

# even_numbers = [x for x in l1 if x % 2 == 0]

# squared_numbers = [x*x for x in l1]

# print(new_list)
# print(squared_numbers)
# print(even_numbers)


#  List Comprehension – Even Numbers from range()
# -----------------------------------------------

# n = 10

# even_numbers = []

# for x in range(0, n+1):
#     if x % 2 == 0:
#         even_numbers.append(x)

# print(even_numbers)