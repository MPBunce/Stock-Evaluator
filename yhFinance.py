import yfinance as yf

stock = yf.Ticker("ZWC.TO")

# get stock info
print("\n")
print(stock.dividends)

print("\n")
# get historical market data
hist = stock.history(period="max")