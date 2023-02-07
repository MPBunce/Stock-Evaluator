import API_Key

import requests
import time

apiKey = API_Key.Token
ticker = input("Please enter a stock ticker: ")    

def getDividends(input_ticker, input_apiKey):
    url = f"https://api.twelvedata.com/dividends?symbol={input_ticker}&range=full&apikey={input_apiKey}"
    response = requests.get(url).json()
    return response

daReturn = getDividends(ticker, apiKey)
print(daReturn)