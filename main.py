#USER INFORMATION STORED
import yfinance as yf
import pandas as pd
def fetchsp(sticker):
	bstock = yf.Ticker(sticker)
	bstockh = bstock.history(period="1d")
	bstockp = float(bstockh.iat[0,1])
	print(bstockp)

user = []

active = True

while active:
    print("Welcome to Fundit! The world's best trading academy!")

    name = input("\nWhat is your username?")

    email = input("\nWhat is your email?")

    capital = input("\nWe are almost there! Think about all the investments you are about to make! What  amount are you willing to invest?")

    password = input("\nNow it's time to secure that capital! Enter a password for your Fundit account.")

    user = name
    user.append(name)
    user.append(email)
    user.append(capital)
    user.append(password)

    stocks = []

    stock = input('What stocks are you currently interested to purschase?')

    fetchsp(stock)

    buy = input('Would you like to buy this stock?')

    if buy == 'Yes':

        stocks.append(stock)

    stock = input('What other stocks are you currently interested to purschase?')
