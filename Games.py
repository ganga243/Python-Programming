# import random
# number = random.randint(1, 100)
# print("Computer number:", number)
# guess = int(input("Guess the number: "))

# if guess == number:
#     print("You won!")
# else:
#     print("Game over!")
#     print("Correct number:", number)
# ----=---------------------------------------------

import math

number = 16
print("Find the square root of:", number)
guess = float(input("Enter your answer: "))
answer = math.sqrt(number)
if guess == answer:
    print("You won!")
else:
    print("Game over!")
    print("Correct answer:", answer)