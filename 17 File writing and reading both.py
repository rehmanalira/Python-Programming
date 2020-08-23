"""
here we first learn about writing and then about both reading and writing

"""
file=open("RA1.txt","a") #"w " spacify that we are going to writing this file as i told "r" is as default
                        # a is used for append mode means we can add data as much we want
file.write("Rehman Ali RA is from faislabad \n if there is probyou can discus")
file.close()


"""
File reading and writing both
"""
file1=open("RA.txt","r+")#r+ is used because we are using both reading and writing
content=file1.read()
print(content)
file1.write("Jutt hundey kury jutt hundey")

file.close()