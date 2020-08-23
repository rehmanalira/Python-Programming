"""
With Block is just a way to open a file without closing it
as we close a file when we open it here we just open it and with
fo all its stuff
"""
with open("RA1.txt") as file:
    c=file.readline()
    print(c)#here there is no need of closing the file
