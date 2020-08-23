"""
Ex -->1
A program which search a word in dictionary and give detail about the
word
"""


#here i created the dictionary and put some words
mydic={
    "set":"It is a collection of Variables"
     ,"python":"It is Programing Languge Mostely used in AI"
    ,"C++":"It is Programing language extendend version of C languge"
    ,"laptop":"A Computer which can be take every where"

       }

print("Enter your word")
word=input()
"""
here is basic logic here we use get() function to get the value
and print it 
"""
print("Your word is",word,"Detail of your word \n",mydic.get(word))


