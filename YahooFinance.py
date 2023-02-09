import yfinance as yf
import pandas as pd
import StockFunctions

# get stock info
stock = yf.Ticker("AQN")


#Get Dividend Info
#StockFunctions.getDividendHistory(stock)

StockFunctions.swedishInvestorRatios(stock)