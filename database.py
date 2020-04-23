import sqlite3

conn = sqlite3.connect("users.db")

c = conn.cursor()

#c.execute("""CREATE TABLE users (
#			name text,
#			password text,
#			capital real,
#			email text
#			)""")

c.execute("INSERT INTO users VALUES ("Jeff","Bezos",5000,"jeff@amazon.com")")

conn.commit()

conn.close()
