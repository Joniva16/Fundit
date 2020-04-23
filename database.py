import sqlite3



class User_info:

	def __init__(self,name,password,capital,email):
		self.name = name
		self.password = password
		self.capital = capital
		self.email = email

conn = sqlite3.connect("users.db")

c = conn.cursor()

#c.execute("""CREATE TABLE users (
#			name text,
#			password text,
#			capital real,
#			email text
#			)""")

def Insert_user(user):
	with conn:
		c.execute("INSERT INTO users VALUES (?,?,?,?)",(user.name,user.password,user.capital,user.email))

user = User_info("Grave","124",10000,"grave@gmail.com")




#c.execute("SELECT * FROM users WHERE password='124'")
#print(c.fetchone())






conn.commit()

conn.close()
