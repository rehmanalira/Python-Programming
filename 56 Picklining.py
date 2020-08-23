import pickle
"""# for serialize the file means packing
obj1=["name"
      "age" 
      "city"
      ]
file_name=("Pickling_file")

f=open(file_name,'wb')

pickle.dump(obj1, f)

f.close()"""
 # for un serilize mean unpacking
file_name="Pickling_file"
f1=open(file_name, "rb")
pickle.load(f1)
f1.close()