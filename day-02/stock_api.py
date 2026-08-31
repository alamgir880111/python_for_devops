import requests
# API_KEY = "6AIAS0KTQWON53JK"
# symbol = "IBM"

# api_url = "https://www.alphavantage.co/"
# query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

# print(api_url+query)

def get_stock_data(symbol):
    
    API_KEY = "6AIAS0KTQWON53JK"
    # symbol = "IBM"

    api_url = "https://www.alphavantage.co/"
    query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url=api_url+query)
    for key,value in response.json().items():
        if key == "Meta Data":
            print(key,value)
    
    
        
    
symbol = input("Enter the symbol: ")    
get_stock_data(symbol)



