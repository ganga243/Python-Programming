# dictionary:key value pair,indexed alla,kodukunna orderil thanne arikum last vare pokunne
#  new student add akan student[ilkodutha mathi]

studstudent.items()
student["name"] = "Anu Ajayan"
student["email"] = "anu@gmail.com"ent ={
    "name" : "Anu",
    "age" : 18,
    "rno" : 2,
    "course" :"BCA",
    "course" :"BCOM"
}
items = student.items()
# print(student)
# print(type(student))
# print(student["age"])
student["name"] = "Anu Ajayan"
# print(student["name"])
student["email"] = "anu@gmail.com"
# print(student)
# print("BCA in student")
# for x in student:
#     print(student[x])
# ---------------------------------------------

# dictionary data get cheyyan[]use cheyithamathi OR get use cheyyam
# key koduthittu illekil default arikum
# existed annel default=>setdefault
# popitem->last item remove cheyyan
# pop->particular ayittudelete cheyyan
# iterable->
# keys->list pole arikum
# forloop vechu access cheyyan pattum
# key illenkil null arikum output
# add cheyunna new datas last arikum add akunnath
# student.item use cheyithu edit cheyithal pinne varunna outpulil change varum athu key ,value affect cheyum




print(student['age'])
print(student.get('age'))
print(student.get('age',20))
student.update({"hobbies":("Reading",Writing)})
student.update ({"rno":4})
student.setdefault("course",BBA)
student.pop('rno')

print(student.values())
print(student.keys())
print()
for key,value in items:
    print(f"{key}:{value}")