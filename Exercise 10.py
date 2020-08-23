"""
It is a program which takes the data from server and the keep it in
file with pickle and also write the data and read with pickle

"""

import requests
import pickle
data=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/")
text=data.text
object1=[text] # save the data in object file

file="shaka_pickle" # file name
f=open(file, "wb") # opening file
print("Pickle write successfully")
pickle.dump(object1, f) # save the data in file
f.close()

f1=open(file, "rb") # reading the file
print("File Read Succfully ")
pickle.load(f1) # load the file with pickle
f1.close()

