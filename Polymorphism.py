# polymorphism-> one name, many forms.
# it is an important concept in oop.
# it makes code more flexible and resusable.

# Syntax

# class ClassName1:
#      def method_name(self):
#        statement

# class ClassName2:
#      def method_name(self):
#         statement

# eg

# class Dog:
#     def speak(self):
#         print("Brak")

# class Cat:
#     def speak(self):
#         print("Meow")
# d=Dog()
# c=Cat()

# d.speak()
# c.speak()


# run-time polymorphism->Dynamic polymorphism
# syntax
# class Parent:
#     def show(self):
#         print("Parent")
# class Child(Parent):
#     def show(self):
#         print("Child")

# obj = Child()
# obj.show()
        
# Eg
# class Shape:
#     def area(self):
#         print("Shape area")
# class Circle(Shape):
#     def area(self):
#         print("Circle area")
# obj = Circle()
# obj.area()


