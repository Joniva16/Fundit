#USER INFORMATION STORED
import yfinance as yf

import pandas as pd

from database import Insert_user

def fetchsp(sticker):
	bstock = yf.Ticker(sticker)
	bstockh = bstock.history(period="1d")
	bstockp = float(bstockh.iat[0,1])
	print(bstockp)
	
class User_info:

	def __init__(self,name,password,capital,email):
		self.name = name
		self.password = password
		self.capital = capital
		self.email = email

user = []

active = True

while active:
    print("Welcome to Fundit! The world's best trading academy!\n")

    name = input("\nWhat is your username?\n")

    email = input("\nWhat is your email?\n")

    capital = input("\nWe are almost there! Think about all the investments you are about to make! What  amount are you willing to invest?\n")

    password = input("\nNow it's time to secure that capital! Enter a password for your Fundit account.\n")

    user = User_info(name, password, capital, email)
    Insert_user(user)

    stocks = []

    stock = input('\nWhat stocks are you currently interested to purschase?\n')

    fetchsp(stock)

    buy = input('\nWould you like to buy this stock?\n')

    if buy == 'Yes':

        stocks.append(stock)

    stock = input('What other stocks are you currently interested to purschase?')
    
