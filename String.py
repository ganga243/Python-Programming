# print("hello world")
 # 29/9/26
 # -------
 #  # PYTHON DATA TYPES
# # -----------------

# # 1.Text
#    # str
# print('hai')
# print("hello")

# # 2.Numeric
#    # Int
#    # Float
#    # Complex 
# print(45)
# print(-45)
# print(5.6)
# print(4+0j)

# # 3.Boolean
#    # Bool
# print(True)
# print(False)

# # 4.Sequence
#     # List
# print([4,5,6])
#     # Tuple
# print((4,4,6))
#     # Range
# print(range(5))

# # 5.Set
#    # Set
# print({4,5,6})
#    # Frozen set
# print(frozenset([7,5,6]))

# # 6.Mapping
#    # Dict
# print({"rno":5,"name":"Angel"})   

# # 7.Binary
#    # Bytes
# print(b"hello")   
#    # Bytearray
# print(bytearray(b"hello"))  
#    # Memoryview
# print(memoryview(b"hello"))

# # 8.None
#   # None
# print(None)

# # check the data-type of a value

# print(type(b"hello"))
# print(type("hello"))
# ---------------------------------------------------
# creating variables
# ------------------
# name="Angel"
# print(name)

# Variable naming rules
# ----------------------

# case-sensitive
# should not start with a number
# donot use special characters
# should be meaningful
# should not use keywords
# can contain digit,alphabets or _
# snake_case
# should  start with a alphabet,digit or _

# name="Angel"
# _name="Angel"
# my-name="sdd"
# my name=""
# if="yadhu"

# name="Amal"
# print(name)
# is_logged_in =True

# a=b=c=10
# p,q,r=56,96,12

# MUTABLE AND IMUTABLE DATA TYPES
# --------------------
# list  
# set
# dict
   
# OPERATORS
# ----------

# 1.Arithmetic 
# -------------
# addition +
# subtraction -
# multiplication *
# division /
# floor division //
# modulus %
# exponentiation **

# eg:
    # a=10
    # b=3
    # print(a+b)
    # print(a-b)
    # print(a*b)
    # print(a/b)
    # print(a//b)
    # print(a%b)
    # print(a**b)

# print(type(a))
# print(int("544644df"))
# print(int(True))
# print(int(False))

# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
# print(2**3**2)
# print(17//15)
# -----------------------------------

# num=int(input("Enter a number:"))


# 5/10/26
# --------
# STRING:seq of characters enclosed in ""/''/
# slicing:starting index positionum ,ending index position um kodkm,step add chym(positive number kodkknm),-ve number kodthal last inu ahn indexing

# name="Alan Mathew"
# course='python programming'
# address="""
# kochi
# kerala
# india
# """
# # type casting
# rno=str(8)

# print(name,course,address)
# print(type(name))   
# print(type(course))
# print(type(address))

# print(name[0])
# print(address[9])

# # slicing:start,end,step
# print(name[0:5])
# print(course[5:16])
# print(course[5:16:2])
# print(course[1:17:3])

# print(name[-1])
# print(name[-2])

# print(course[-10:-1])
# print(course[-10:-1:2])
# print(course[:5])
# print(course[5])
# print(name[4:])
# print(course[::2])
# print(course[::-1])

# ---------------------------------

# string methods
# --------------
name="Alan Mathew"
print(name.upper())
print(name.lower())
print(name.capitalize()) 
print(name.title())
print(name.swapcase())
print(name.startswith(('Ala')))
print(name.endswith('Hew'))
print(name.isalpha())
print(name.isdigit())
print('hfak6455'.isalnum())
print(name.strip()+'dfdf')
print(name.lstrip()+'dfdf')
print(name.rstrip()+'dfdf')

print(name.split(''))
print(name.split('a'))

# format function(nle nokknm)