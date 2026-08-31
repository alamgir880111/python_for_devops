import requests


jokes_url = "https://official-joke-api.appspot.com/random_joke"
dad_jokes_url = "https://icanhazdadjoke.com/"

def jokes_function(url_type):
    
    
    if mood == "dad":
        headers = {"Accept" : "application/json"}
        response = requests.get(url = url_type, headers = headers)
        final_jokes =  response.json() ["joke"]
        
    elif mood == "pj":
        response = requests.get(url = url_type)

        final_jokes = response.json() ["setup"]  + response.json() ["punchline"]
    
    return final_jokes

mood = input("Which jokes do you like. ex(dad or pj)")
if mood == "dad":
    url_type = dad_jokes_url
    
elif mood == "pj":
    url_type =jokes_url
    
final_result = jokes_function(url_type)
print(final_result)


