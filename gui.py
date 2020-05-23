from tkinter import *

def credentials():
	log = Tk()
	log.geometry("500x600")
	log.title("Fundit")

	#Displaying the main logo on the sign in page
	logo = Image.open("logo.png")
	logo_render = ImageTk.Photoimage(logo)
	lbl_logo = Label(log, image=logo_render)
	lbl_logo.image = logo_render
	lbl_logo.pack(fill=X)

	log.mainloop()

credentials()