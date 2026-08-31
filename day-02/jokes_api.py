def jokes_function():
    import requests

    jokes_url = "https://official-joke-api.appspot.com/random_joke"

    response = requests.get(url = jokes_url)

    final_jokes = response.json() ["setup"] + response.json() ["punchline"]
    
    print(final_jokes)
    
jokes_function()






