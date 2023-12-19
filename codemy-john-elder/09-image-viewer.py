import os
from tkinter import *
from PIL import ImageTk, Image

root = Tk()

# Setting title and icon
root.title("The Turtle Tourer")
# https://stackoverflow.com/a/11180300/10645311
img = PhotoImage(file='images/current-icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)

my_img_1 = ImageTk.PhotoImage(Image.open('images/unsplash/ana-singh-small.jpg'))
my_img_2 = ImageTk.PhotoImage(Image.open('images/unsplash/erin-simmons-small.jpg'))
my_img_3 = ImageTk.PhotoImage(Image.open('images/unsplash/francesco-ungaro-small.jpg'))
my_img_4 = ImageTk.PhotoImage(Image.open('images/unsplash/jeremy-bishop-small.jpg'))
my_img_5 = ImageTk.PhotoImage(Image.open('images/unsplash/randall-ruiz-small.jpg'))

image_list = [my_img_1, my_img_2, my_img_3, my_img_4, my_img_5]

my_label = Label(image=my_img_1)

def forward(image_number):
  global my_label
  global button_forward
  global button_back

  my_label.grid_forget()
  my_label = Label(image=image_list[image_number - 1])
  button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
  button_back = Button(root, text="<<", command=lambda: back(image_number-1))

  if image_number == 5:
    button_forward = Button(root, text=">>", state=DISABLED)

  my_label.grid(row=0, column=0, columnspan=3)
  button_back.grid(row=1, column=0)
  button_forward.grid(row=1, column=2)

def back(image_number):
  global my_label
  global button_forward
  global button_back

  my_label.grid_forget()
  my_label = Label(image=image_list[image_number - 1])
  button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
  button_back = Button(root, text="<<", command=lambda: back(image_number-1))

  if image_number == 1:
    button_back = Button(root, text="<<", state=DISABLED)

  my_label.grid(row=0, column=0, columnspan=3)
  button_back.grid(row=1, column=0)
  button_forward.grid(row=1, column=2)

button_back = Button(root, text="<<", command=lambda: back(0), state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

my_label.grid(row=0, column=0, columnspan=3)
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
