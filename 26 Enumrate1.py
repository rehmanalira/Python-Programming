"""
Enumrate keyword means that it become esasy for us to get  the locatio or what
we want to remove thing in our list

"""
l=["Rehman","Rizwan","Tayyab","Ahsan","jutt"]

for index,item in enumerate(l):#index give the position []<-- index position and item will give the items
    if index%2==0:#it means it give thoes items that give zero means even
        print("NAmes are", item)