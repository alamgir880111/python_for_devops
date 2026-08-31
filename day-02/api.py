import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)

for key,value in response.json().items():
    print(key,value)