import sqlite3


conn = sqlite3.connect("users.db")

c = conn.cursor()

#c.execute("""CREATE TABLE users (
#			name text,
#			password text,
#			capital real,
#			email text
#			)""")



def insert_user(name,password,capital,email):
	with conn:
		c.execute("INSERT INTO users VALUES (name,password,capital,email)")

insert_user("Bob","12345",25,"bob@gmail.com")


conn.commit()

conn.close()
