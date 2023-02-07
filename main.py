import API_Key
import json
import requests
import time

apiKey = API_Key.Token
ticker = input("Please enter a stock ticker: ")    

def getDividends(input_ticker, input_apiKey):
    url = f"https://api.twelvedata.com/dividends?symbol={input_ticker}&range=full&apikey={input_apiKey}"
    response = requests.get(url).json()
    response_string = json.dumps(response)
    my_dict = json.loads(response_string)
    return my_dict

daReturn = getDividends(ticker, apiKey)
for date in daReturn:
    print(daReturn[date])
    print("\n\n")