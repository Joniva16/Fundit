#USER INFORMATION STORED


import pandas as pd

#This function allows to fetch a stock price using its ticker symbol
#For example you can use fetchsp("AAPL")
import yfinance as yf

def fetchsp(sticker):
	bstock = yf.Ticker(sticker)
	bstockh = bstock.history(period="1d")
	bstockp = float(bstockh.iat[0,1])
	return bstockp

print(fetchsp("AAPL"))