"""
tell and seek are the two keywords in which we
tell give information about the where or from which line our text is staring
and seek
seek will starts our pointer from the point where we write
"""
file=open("RA.txt")
print(file.tell())#it will tell from which we are starting our file reading
print(file.readline())
print(file.tell())#from which point we start it tells eg->here it is at 15.
print(file.readline())#it will print the character line by line
print(file.tell())
print(file.seek(23))#it tells that where we start our line
print(file.readline())

file.close()