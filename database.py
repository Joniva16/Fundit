import sqlite3



class User_info:

	def __init__(self,name,password,capital,email):
		self.name = name
		self.password = password
		self.capital = capital

conn = sqlite3.connect("users.db")

c = conn.cursor()

c.execute("""CREATE TABLE users (
			name text,
			password text,
			capital real,
			)""")

#This function will allow you to insert a user in the following fashion
#user = User_info("Grave","124",10000,"grave@gmail.com"
def Insert_user(user):
	with conn:
		c.execute("INSERT INTO users VALUES (?,?,?,)",(user.name,user.password,user.capital))


#THis function will allow you to search for users in the databse according to
#Parameters like password or name
#c.execute("SELECT * FROM users WHERE password='124'")
#print(c.fetchone())






conn.commit()

conn.close()


#WORK BELOW THIS 