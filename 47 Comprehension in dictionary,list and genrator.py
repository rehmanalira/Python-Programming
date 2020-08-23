"""
Comprehension ;
it is basically way to write thre lines of code in just one line by writing list or dictionary or by
genrator

"""


print("Enter the number at which you want to genrate")
num=int(input())
print("for list press 1")
print("for dictionary press 2")
print("for genrator press 3")
ch=int(input())
if ch == 1:
    list1=[i for i in range(num) if i%3==0]
    print(list1)
if ch == 2:
    dict1={i:f"item{i}" for i in range(num)}
    print(dict1)
    dict2={value:key for key,value in dict1.items()}
    print(dict2)
if ch == 3:
    gen=(i for i in range(num))
    print(gen.__next__())
    print(gen.__next__())