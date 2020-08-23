# j son is used to storing and exchange of data
# javascript object notation json

# if we have a string in json and want to conver into python we used
#json.load
import json
data='{"name": "RA" , "Age" :"20"}'
y=json.loads(data)
print(y["name"])

# if we have python strings and want to convert into the json we use
#json.dumps
data1={ # this is pythin data
    "Name": "RA JUTT",
    "Age": "19"
}
l=json.dumps(data1)
print(l)