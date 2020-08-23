mystr="Rehman Ali Sagar from Faislabad"
print(len(mystr),"words") #this will give how many words are in string
print(mystr[0:32:2])
"""
1-->in this we give the position of the letter [0:] in first colon it  tells where from
string starts means 0 and if we not give it also starts it from 0
2--> the next colon is[0:3] it means that how much long you goes means here we give 
last number of string where we end our string
3--> the last colon [0:3:2] gives the spaces how much we want if we start from 2 it
give 1 space and dont write the one word after 1 space means first  it take R and
the space and the h,

"""
#SO what happen if we use -3 or
print("- Values")
print(mystr[:-5])
"""
1--> when we start writingg from the - value then in first colon[-3:] it starts 
from the end and print only how many value give and it print only thoes
2--> if we starts from the second colon then it will print [:-2] all except last
words which we give in the in order
3--> if we give [::-1]
then it will written whole string in opposit direction

"""
 #Functions in string

print(mystr.upper()) #it will upper all the letter
print(mystr.lower()) #it will lower all the letter
print(mystr.capitalize()) #it will captalize the first letter
print(mystr.count("r")) #it will count how many string or "r" which i pass haveing
print(mystr.find("Ali")) #it will find the letter tells its index position
print(mystr.replace("Sagar","RA")) #it will replace the word from
