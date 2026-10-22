# Part 1: Basic List
# 1. Find the Largest Element
# ------------------------------------
# numbers = [10, 5, 25, 8, 15]

# largest = numbers[0]

# for i in numbers:
#     if i > largest:
#         largest = i

# print("Largest element:", largest)

# 2. Find the Smallest Element
# ---------------------------------------
# numbers = [10, 5, 25, 8, 15]

# smallest = numbers[0]

# for i in numbers:
#     if i < smallest:
#         smallest = i

# print("Smallest element:", smallest)

# 3. Find Sum of All Elements
# ----------------------------------
# numbers = [1, 2, 3, 4, 5]

# total = 0

# for i in numbers:
#     total = total + i

# print("Sum:", total)

# 4. Find Average of Elements
# ---------------------------------------
# numbers = [10, 20, 30, 40, 50]

# total = 0

# for i in numbers:
#     total = total + i

# average = total / len(numbers)

# print("Average:", average)

# 5. Reverse a List Without Using reverse()
# -------------------------------------------------
# numbers = [1, 2, 3, 4, 5]

# reversed_list = []

# for i in numbers:
#     reversed_list.insert(0, i)

# print(reversed_list)

# Part 2: Logic-Based List
# 1. Remove Duplicates
# -----------------------------------------
# numbers = [1, 2, 2, 3, 4, 4, 5]

# unique = []

# for i in numbers:
#     if i not in unique:
#         unique.append(i)

# print(unique)

# 2. Find Second Largest Number
# -------------------------------------
# numbers = [10, 20, 50, 40, 30]

# largest = numbers[0]
# second_largest = numbers[0]

# for i in numbers:
#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif i > second_largest and i < largest:
#         second_largest = i

# print("Second largest:", second_largest)

# 3. Separate Even and Odd Numbers
# ---------------------------------------------
# numbers = [1, 2, 3, 4, 5, 6]
# even = []
# odd = []

# for i in numbers:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print("Even numbers:", even)
# print("Odd numbers:", odd)

# 4. Find Common Elements Between Two Lists.
# ---------------------------------------------------
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# common = []

# for i in list1:
#     if i in list2:
#         common.append(i)

# print("Common elements:", common)

# 5. Merge Two Lists Without Duplicates
# ------------------------------------------------
# list1 = [1, 2, 3]
# list2 = [3, 4, 5]
# merged = []

# for i in list1:
#     if i not in merged:
#         merged.append(i)

# for i in list2:
#     if i not in merged:
#         merged.append(i)

# print(merged)

# Part 3: Nested List Questions
# 1. Sum of All Elements in a Matrix
# -------------------------------------------
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# total = 0

# for row in matrix:
#     for i in row:
#         total = total + i

# print("Sum:", total)

# 2. Find Largest Element in a Matrix
# -----------------------------------------------
# matrix = [
#     [1, 2, 3],
#     [10, 5, 6],
#     [7, 8, 9]
# ]

# largest = matrix[0][0]

# for row in matrix:
#     for i in row:
#         if i > largest:
#             largest = i

# print("Largest element:", largest)