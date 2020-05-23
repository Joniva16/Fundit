from tkinter import *
from PIL import Image, ImageTk
from datastorage import Insert_user
import sqlite3

conn = sqlite3.connect("users.db")

c = conn.cursor()

def credentials():

	global font

	log = Tk()
	log.geometry("500x600")
	log.title("Fundit")
	log.configure(background="white")
	log.resizable(width=False, height=False)

	#Displaying the main logo on the sign in page
	logo = Image.open("media/logo.png")
	render = ImageTk.PhotoImage(logo)
	lbl_logo = Label(log, image=render, bg="white")
	lbl_logo.image = render
	lbl_logo.pack(fill=X)

	#Creating the frame for the entrys

	frame_entry1= Frame(log,width=500, height=300, bg="white")
	frame_entry1.place(x=60,y=230)



	#Font specifications
	font = ("Helvetica", 20,"bold")
	font_color = "#9acc56"

	#Username entry and password

	#Username label
	enter_username = Label(frame_entry1,text="Username:",bg="white",fg="black",font=font)
	enter_username.pack(anchor=W)

	#Username entry
	entry_username = Entry(frame_entry1,bg="white",width=20,font=("Helvetica", 15),fg="black")
	entry_username.pack()





	frame_entry2= Frame(log,width=500, height=100, bg="white")
	frame_entry2.place(x=60,y=330)


	#Password label
	enter_password = Label(frame_entry2,text="Password:",bg="white",fg="black",font=font)
	enter_password.pack(anchor=W)

	#Password entry
	entry_password = Entry(frame_entry2,bg="white",width=20,font=("Helvetica", 15),fg="black")
	entry_password.pack()

	frame_avail_name= Frame(log,width=500, height=500, bg="white")
	frame_avail_name.place(x=60,y=300)

	avail_response_name = Label(frame_avail_name,text="",bg="white",fg="black",font=("Helvetica", 15))
	avail_response_name.pack()

	frame_avail_pass= Frame(log,width=500, height=500, bg="white")
	frame_avail_pass.place(x=60,y=400)

	avail_response_pass = Label(frame_avail_pass,text="",bg="white",fg="black",font=("Helvetica", 15))
	avail_response_pass.pack()

	def adduser():
		username = str(entry_username.get())
		password = str(entry_password.get())

		if password == "":
			avail_response_pass.configure(text="Please enter a password",fg="Red")
		else:

			try:
				avail_response_pass.configure(text="",fg="Red")
				c.execute(f"SELECT * FROM users WHERE name='{username}'")
				username_avail = c.fetchone()[0]
				print("This username has already been taken")
				avail_response_name.configure(text="This username has already been taken",fg="Red")


			except TypeError:
				avail_response_pass.configure(text="",fg="Red")
				print("This username is available")
				avail_response_name.configure(text="This username is available",fg="Green")

	frame_button_entry= Frame(log,width=500, height=50, bg="white")
	frame_button_entry.place(x=165,y=450)



	entry_button_register = Button(frame_button_entry,bg="#9acc56",text="Register",font=("Helvetica", 15),command=adduser)
	entry_button_register.pack(side=LEFT)

	entry_button_login = Button(frame_button_entry,bg="#9acc56",text=" Login ",font=("Helvetica", 15))
	entry_button_login.pack(side=LEFT,padx=15)



	#Keeping the window active
	log.mainloop()


credentials()

conn.commit()

conn.close()