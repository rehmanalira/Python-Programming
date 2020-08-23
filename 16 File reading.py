
"""
here we are learning all about file reading

"""

file=open("RA.txt")
#content=file.read()#if we pass the argument then it will print only what we argument pass in it
#print(content)
#for line in content:
#print(line) # it will print it charcater by character

print(file.readline())# it will print the line by line
print(file.readline())
print(file.readlines()) # it willl give full detail what are we doing where is space

file.close()