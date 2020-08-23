import requests
x=requests.get("http://www.youtube.com")
print(x.text)

#requests.post it will send your data to the website
url="https://www.google.com"
data={"name": "RA"}
x=requests.post(url=url,data=data)
print(x.text)