
print("Enter Number")
num1=int(input())
print("Enter True or False")
num2=int(input())
if num2==1:
    rows = num1
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')


    print("")


else:
    rows = num1
    for i in range(rows + 1, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print(" ")