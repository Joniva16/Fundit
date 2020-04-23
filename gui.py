from tkinter import *

root = Tk()
root.geometry("700x400")
root.title("Fundit")
root.configure(background="white")

frame_input= Frame(root,width=500,height=500,background="white")
frame_input.place(x=0,y=0)

lbl_time = Label(frame_input,text="What is your username?", font=(13),background="white")
lbl_time.place(x=10,y=10)

entry_time = Entry(frame_input,bg="white",width=25)
entry_time.place(x=200,y=10)

frame_input2= Frame(root,width=500,height=400,background="white")
frame_input2.place(x=0,y=0)

lbl_time4 = Label(frame_input2,text="What is your password?", font=(13),background="white")
lbl_time4.place(x=10,y=60)

entry_time5 = Entry(frame_input2,bg="white",width=25)
entry_time5.place(x=200,y=60)

lbl_time4 = Label(frame_input2,text="What is your capital?", font=(13),background="white")
lbl_time4.place(x=10,y=110)

entry_time5 = Entry(frame_input2,bg="white",width=25)
entry_time5.place(x=200,y=110)

lbl_time4 = Label(frame_input2,text="What is your email?", font=(13),background="white")
lbl_time4.place(x=10,y=160)

entry_time5 = Entry(frame_input2,bg="white",width=25)
entry_time5.place(x=200,y=160)



root.mainloop()