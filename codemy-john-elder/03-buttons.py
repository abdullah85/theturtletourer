from tkinter import *

root = Tk()

def myClick():
  myLabel=Label(root, text="Button was Clicked!")
  myLabel.pack()

myButton = Button(root, text="Click me", padx=50, pady=5, command=myClick, fg="white", bg="#000000")
myButton.pack()

root.mainloop()