from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=3)
e.pack()
e.insert(0, "Enter Your Name: ")

def myClick():
  msg = "Hello " + e.get()
  myLabel=Label(root, text=msg)
  myLabel.pack()

myButton = Button(root, text="Enter Your Name", padx=50, pady=5, command=myClick)
myButton.pack()

root.mainloop()