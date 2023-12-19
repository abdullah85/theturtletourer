from tkinter import *

root = Tk()
# Setting title and icon
root.title("The Turtle Tourer")
# https://stackoverflow.com/a/11180300/10645311
img = PhotoImage(file='images/current-icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)

frame = LabelFrame(root, text="This is my Frame ...", padx=50, pady=50)
frame.pack(padx=50, pady=10)
b = Button(frame, text="Click Here to Exit", command=root.quit)
b.grid(row=0, column=0)
b2 = Button(frame, text="Second Button")
b2.grid(row=1, column=1)

root.mainloop()