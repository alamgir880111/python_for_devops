import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)

for key,value in response.json().items():
    if key == "id":
        if value in [1,4,5,6]:
            print ("This is valid")