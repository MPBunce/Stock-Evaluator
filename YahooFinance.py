import yfinance as yf
import pandas as pd
import StockFunctions
stock = yf.Ticker("AQN")

# get stock info
print("\n")
StockFunctions.getDividendInfo(stock)
