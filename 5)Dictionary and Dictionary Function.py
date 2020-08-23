d1={"RA":"Roti","rizwan":"pani","h":"LM"}

print(d1["RA"])#it simply gives the value which is after by the colon
#what if i want to add the new dictionry or new member
#there are two way 1--> is

d1["shaka"]="Ching Hung"
print(d1)#by this way we will add this to
#second 2--> way we just we add the update
d1.update({"hi":"this"})#update way is the best way to add the new item
#in the list we must have to use {}
print(d1)
#what if we want to delete
del d1["shaka"]
print(d1)
print(d1.items())#it will give the items of the list
print(d1.keys())#it will give the which keys we haveing
