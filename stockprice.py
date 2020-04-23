import yfinance as yf 
import pandas as pd

#This is a function to fetch the stock price
#bstock is a reference to the bought stock
#bstockh is a reference to the bought stock's history
#bstockp is a reference to the bought stock's price

def fetchsp(sticker):
	bstock = yf.Ticker(sticker)
	bstockh = bstock.history(period="1d")
	print(bstockh)
	bstockp = float(bstockh.iat[0,1])
	print(bstockp)

