#!/usr/bin/python
import os
from tkinter import *
from tkinter import ttk
import turtle

root = Tk()
# Setting title and icon
root.title("Tour The Turtle")
try:
  relative_path = 'images/logos/current-logo.png'
  absolute_path = os.path.dirname(__file__)
  full_path = os.path.join(absolute_path, relative_path)
  img = PhotoImage(file=full_path)
  root.tk.call('wm', 'iconphoto', root._w, img)
except:
  print('Could not set icon image')

root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

# Initialize turtle with canvas section
turtleCanvas = turtle.ScrolledCanvas(root)
turtleCanvas.grid(column=0, row=0, sticky=(N, W, E, S), columnspan=1)
global turtle1

# Initialize functions for turtle
def turtle_forward():
  distance = int(forward_entry.get())
  turtle1.forward(distance)

def turtle_turn():
  angle = int(angle_entry.get())
  direction = direction_list.get()
  if(direction == 'right'):
    turtle1.right(angle)
  else:
    turtle1.left(angle)

def turtle_home():
  turtle1.home()

def turtle_clear():
  turtle1.clear()

turtle1 = turtle.RawTurtle(turtleCanvas)
turtle1.shape('turtle')
control_frame = ttk.Frame(root)

# Define all buttons to add to control frame
# Movement
movement_frame = LabelFrame(control_frame, text="Move", padx=15, pady=15)
forward_entry = Entry(movement_frame, width=17, borderwidth=3)
forward_entry.insert(0, "135")

angle_entry = Entry(movement_frame, width=17, borderwidth=3)
angle_entry.insert(0, "45")
direction_values = StringVar(value="right")
direction_list = ttk.Combobox(movement_frame, textvariable=direction_values)
direction_list['values'] = ('right', 'left')

forward_button = Button(movement_frame, text="Forward", command=turtle_forward, padx=19, pady=7)
turn_button = Button(movement_frame, text="Turn", command=turtle_turn, padx=19, pady=7)
home_button = Button(movement_frame, text="Home", command=turtle_home, padx=31, pady=7)
clear_button = Button(movement_frame, text="Clear Drawing", command=turtle_clear, padx=31, pady=7)
angle_entry.grid(row=1,column=0)
direction_list.grid(row=1, column=1)
turn_button.grid(column=0, row=2, sticky=W+E)

forward_button.grid(column=1, row=0, sticky=W+E)
forward_entry.grid(column=0, row=0, padx=15, pady=15)
home_button.grid(column=0, row=3, sticky=W+E)
clear_button.grid(column=1, row=3, sticky=W+E)

# Turtle Styling
style_frame = LabelFrame(control_frame, text="Style", padx=15, pady=15)
turtle_shape_label = Label(style_frame, text="Shape", padx = 45, pady=7)
shape_values = StringVar(value="turtle")
shape_list = ttk.Combobox(style_frame, textvariable=shape_values)
shape_list.grid(column=1, row=0)
turtle_shape_label.grid(column=0, row=0)
shape_list.bind('<<ComboboxSelected>>', lambda x: change_shape(x))
shape_list['values']= ('arrow', 'circle', 'turtle',  'square', 'triangle', 'classic')

# Lay the frames out appropriately
control_frame.grid(column=1,row=0, padx=15)
movement_frame.pack()
style_frame.pack()

def change_shape(e):
  new_shape = shape_list.get()
  turtle1.shape(new_shape)
  # turtle1
  return

root.mainloop()