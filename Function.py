# # Functions are resusable block of codes that we use to perform a specific task, created using a def keyword
# def function_name(parameters):
#     function body
#     return
    
# function_name(arguments) #function invoking

# def add(a,b):
#     result = a+b
#     return result
# # print(add(a,b))
# # print(print(add(45,78)))
# print(print(add(45,78)))
# print(type(print(add(45,78))))
# print(print(type(add(45,78))))

# print(add(23,86))
# print(add(70,7))
# print(add(1,2))
# print(result)
# pass cheyunna value->argument
#-----------------------------------------------------------------------------------------------------------------------
# default parameters last kodukavuu
# keyword argument->function call cheyunna tymil parameter name use cheyithu value tharunnath anuu keyword
# arbitrary argument-> oru functionil any number of argument using *args(,separated ayittu value koduthale work aguu)
# *args-il use cheyunna colletion->tuple
# kwargs use cheyunna datatype->dictionary
# lambda function->anonimous function,name kanill,
# one-line function use cheyyan vendi,oru function write cheyunna simplest method
# square = lambda x :-> ee colon kazhiju varunnath arikum return cheyunnath
# single line if statement kodukunnath->compactive statement
# synatax in compactive: trueExpression if condition else falseExpression
# -----------------------------------------------------------------------------------------------------------------------------


# def greet(user,msg="Good Morning!!"):  #default parameter
#     print(f"Hello,{user} {msg}")

# greet("Alan")
# greet("Amal","Good Morning!!")

# greet(msg="Good Evening",user="jithu") #keyword arguments

# def display_numbers(*args):
#     print(args)

# display_numbers(12,4,68,76,100,1,42)  #arbitrary arguments
# display_numbers(1)
# display_numbers(22,3,50)

# def display_students(**kwargs):
#     print(kwargs)

# display_students(name="Anu",age=17)  #arabitrary keyword argument

# # lambda parameter : expression
# # def square_number(x)
#     #   return x*x
# # TrueExpression if condition else falseExpression
# square = lambda x : x*x
# print(square(5))
# # n = 45
# # postive
# # negative
# # Zero

# number_type = lambda x:"positive" if x > 0  else "Negative" if x <0 else "Zero"

# print(number_type(10))
# print(number_type(0))
# print(number_type(-10))



