import sqlite3



class User_info:

	def __init__(self,name,password,capital):
		self.name = name
		self.password = password
		self.capital = capital

conn = sqlite3.connect("users.db")

c = conn.cursor()

#c.execute("""CREATE TABLE users (
#			name text,
#			password text,
#			capital real
#			)""")

#This function will allow you to insert a user in the following fashion
#user = User_info("Grave","124",10000,"grave@gmail.com")
def Insert_user(user):
	with conn:
		c.execute("INSERT INTO users VALUES (?,?,?)",(user.name,user.password,user.capital))
		print("A new user has been inserted into the database")


#THis function will allow you to search for users in the databse according to
#Parameters like password or name



conn.commit()

conn.close()


#WORK BELOW THIS 