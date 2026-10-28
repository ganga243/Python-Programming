# s1 = {4,5,6,9}
# l1 = ["python","js","js","Flutter","DS","DS","DA","Python"]
# courses = []
# for course in l1:
#     if course not in courses:
#         courses.append(course)
# print(courses)
# s2 = set(l1)
# print(s2)
# s3 = {45,89,89,76,"Alan","Alan",45}
# print(type(s2))

# print(s1)
# print(len(s3))
# print(s3)

# # new_set = {1,True,45,"Hello","",0,False}
# # print(new_set)
# # print(0 in new_set)
# # for s in s1:
# #     print(s)

# new_set ={1,True,45,"Hello","",0,False}
# new_set.discard("Hello")
# new_set.add("HelloWorld")

# print(new_set)

# s1.add("Python Programming")
# s1.update([88,89,45,4,5,6])
# s1.remove("Python Programming")
# # s1.remove("Python Programming")  #generate an error if not present
# s1.discard("Python Programming") #removes the element if exists and deos not generate an error if does not exist
# s1.pop()
# s1.clear()
# print(s1)

python = {"Hari","Anu","Amal","Kiran","Kuttu"}
mern = {"Arun","Anju","Kavya","Reeba"}


print(python.union(mern))
print(python | mern )
print(python.intersection(mern))
print(python & mern)
print(python.symmetric_difference(mern))
print(python ^ mern)
print(python.difference(mern))
print(python -mern)
print(mern.difference(python))
print(mern - python)




numbers = {20,40,1,2,3,5,6,8,11,13,26,35,42,0}
even_numbers = {20,40,2,6,8,26,42,0,1224}

print(numbers.issuperset(even_numbers))
print(even_numbers.issubset(numbers))
print({1,2}.issubset({1,2}))
print({1,2}.issubset({1,2,3}))
print({1,2,3,4}.issubset({1,2,3}))
print({1,2,3,4}.issuperset({1,2,3,4}))
print({1,3,5}.isdisjoint({2,4,6}))
print({1,3,5}.issubset({2,4,5,6}))