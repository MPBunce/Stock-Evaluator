import API_Key
from twelvedata import TDClient

ticker = input("Please enter a stock ticker: ")    

td = TDClient(apikey=API_Key.Token)

expirations = td.get_options_expiration(
    symbol="AAPL",
).as_json()['dates']

put_options = td.get_options_chain(
    symbol="AAPL",
    side="put",
    expiration_date=expirations[0]
).as_json()['puts']

print(put_options)