# # list is a collection of hetrogenegous data
# # Orderd
# #Indexed
# #Allow duplicates

# numbers =[45,870,110,134,1550,155]
# print(numbers)
# print(type(numbers))
# print(len(numbers))

# print(numbers[3])
# print(numbers[0:3])
# print(numbers[0:5:2])
# print(numbers[::-1])
# print(numbers[-1])

# numbers[2] = 1

# print(numbers)

# for n in numbers:
#     print(n)

# print('Even numbers')
# for n in numbers:
#     if n%2 == 0:
#         # print(n)

# 
# a = [10,20,30]
# a.append(40)
# print(a)

# extends(iterable)---
# a=[10,20]
# a.extend([30,40])
# print(a)

# insert(i,x)---
# a=[10,20,30]
# a.insert(1,15)
# print(a)

# remove(x)----
# a=[10,20,40,30]
# a.remove(20)
# print(a)

# pop(i)---
# a=[10,20,30]
# x=a.pop()
# print(x)
# print(a)

# clear()---
# a=[10,20,30]
# a.clear()
# print(a)

# index(x)---
# a=[10,20,30]
# print(a.index(20))

# count(x)---
# a=[10,20,20,30]
# print(a.count(20))

# sort()---
# a=[30,10,45,65]
# a.sort()
# print(a)

# reverse()---
# a=[10,30,40,50]
# a.reverse()
# print(a)

# copy()
# a=[10,20,30,40,60,50]
# b = a.copy()
# print(b)


names = ["Aryan", "Arun", "Anu", "Meenu", "Jechin"]

names.append("Adith")
names.append("Amala")
names.insert(2, "Athul")
names.extend(["Pranav", "Sreekanth", "Suriya", "Vijay", "Ajith", "Athul"])
names.remove("Ajith")
names.pop(2)

# names.pop()
# del names[0]
# del names
# names.clear()

print(names.index("Suriya"))
print(names.count("Athul"))
# # names.sort()
# # names.reverse()

# names.append([1, 2, 3])
# copy_names = names.copy()
# copy_names[5] = "Vimal"
# names[-1][2] = 86

# print(names[-1])
# print(copy_names)


for name in names:
    #  if name[0] == "A": if name.startswitch('A)
          print(name)


