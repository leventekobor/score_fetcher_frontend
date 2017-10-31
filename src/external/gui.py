from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("100x100")


def refresh():
	msg = messagebox.showinfo("Message" , "Refreshed!")


B = Button(top, text = "Refresh", command = refresh)
B.place(x = 50, y = 50)


top.mainloop()