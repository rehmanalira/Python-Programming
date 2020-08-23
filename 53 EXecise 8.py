"""

NOt COmplerted
input --> directory/folder
 check -->files
 agr files the first letter is small
 --> Capital
 agr --> jpg file
 --> number dey dey ga 1.jpg or 2.jpg
 ek file jino asi capital ni krna chanda

"""
import  os
path_name=str(input("Enter the Path :"))
file_name=str(input("File name "))
path_name=path_name + file_name

try:
    os.chdir(path_name)
    print(os.listdir(path_name))
    print(os.getcwd())
except Exception as e:
    print(e)
v="text.txt"
for root,dirs,files in os.walk(path_name):
    if v in files:
        print("Yes it is")

        print("It is capatilized succefuly")


    else:
        print("It is not")
print(os.getcwd())

for root,dirs,files in os.walk(path_name):
    if file_name.endswith(".jbg") in files:
        print("Yes it is images")
    else:
        print("NO ")
print(os.getcwd())