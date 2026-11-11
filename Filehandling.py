# 
# open function annu use cheyunnath first(file function open cheyitha close cheyithirikannam)
# mode->
# readline->single line read cheyyan(one line at a tym)
# readlines->ellam lineile list orumichu tharanan(list of all lines)
# write()->oru file illathu anne aa file create cheyyum nammalu kodukunna content add agum(ulla filene replace cheyithu vekum)
# writelines-->
# a->append
# seek()->cursor ethu positionileku pookan vendi
# tell()->cursor evide annu ennu ullath
# module->kure  pakages ulathine annu pakage
# import use cheyunna syntax:-from,filename,module
# framework->django,bulit in functions ind,ivide use cheyyan padu ullu ennu paraja 
# 


# open(filename,mode)
# file=None
try :
    file = open('names.txt','r')
    print(file.read())
except FileNotFoundError:
    print("Wrong filename")
else:
    file.close()
# file = open('names.txt','r')
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# print(file.readlines()) #list of all lines
# file = open('sample.txt','w')
# file.write("Python Programming\n")
# file.write(["Django\n","FastAPI\n","DRF"])
# file = open('sample.txt','a')
# file.write("/nFlask")
# file.close()

with open('names.txt') as file:
    file.seek(9)
    print(file.read(5))
    print(file.tell())
    print(file.read(5))
    print(file.tell())



