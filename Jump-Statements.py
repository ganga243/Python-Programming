# while condition:
#     block of loop

# while 1<10:
#     pass

# n=1
# while n<=10:
#     if(n==4):
#         break    #Terminates a loop
#     print(n)
#     n+=1

n = 1

while n <= 10:
    if n == 4:
        n += 1
        continue

    print(n)
    n += 1


# Iteration 1
# n=1
# 1<=10 --> True
#     1 == 4 --> False
#     n=2

# Iteration 2
# n = 2
# 2 <= 10 --> True
#     2 == 4 --> False 
#     n=3

# Iteration 3
# n = 2
# 2 <= 10 --> True
#     2 == 4 --> False 
#     n=3


# Iteration 4
# n = 4
# 4 <= 10 --> True
#     4 == 4 --> True
#     continue


# Iteration 5
# n = 4
# 4 <= 10 --> True
#     4 == 4 --> True
#     continue

# output
# 1
# 2
# 3

n = int(input("Enter a multi-digit number: "))

sum = 0

while n > 0:
    r = n % 10
    sum += r
    n //= 10

print(f"Sum is {sum}")


# Iteration 1
# n = 487
# r = 487 % 10 = 7
# sum = 0 + 7 = 7
# n = 487 // 10 = 48

# Iteration 2
# n = 48
# r = 48 % 10 = 8
# sum = 7 + 8 = 15
# n = 48 // 10 = 4

# Iteration 3
# n = 4
# r = 4 % 10 = 4
# sum = 15 + 4 = 19
# n = 4 // 10 = 0

# Output
# Sum is 19

