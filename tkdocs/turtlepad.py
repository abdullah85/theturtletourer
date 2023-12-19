from tkinter import *
from tkinter import ttk
import turtle

root = Tk()
root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

turtleCanvas = turtle.ScrolledCanvas(root)
turtleCanvas.grid(column=0, row=0, sticky=(N, W, E, S), columnspan=1)
global turtle1
turtle1 = turtle.RawTurtle(turtleCanvas)
turtle1.shape('turtle')
control_frame = ttk.Frame(root)
control_frame.grid(column=1,row=0, padx=15)

# Define all buttons to add to control frame
forward_entry = Entry(control_frame, width=17, borderwidth=3)

def turtle_forward():
  distance = int(forward_entry.get())
  turtle1.forward(distance)

def turtle_home():
  turtle1.home()

def turtle_clear():
  turtle1.clear()

def turtle_left_90():
  turtle1.left(90)

def turtle_right_90():
  turtle1.right(90)

# Movement
forward_button = Button(control_frame, text="Forward", command=turtle_forward, padx=19, pady=7)
left_90_button = Button(control_frame, text="Left by 90", command=turtle_left_90, padx=17, pady=7)
right_90_button = Button(control_frame, text="Right by 90", command=turtle_right_90, padx=11, pady=7)

# Miscellaneuous
home_button = Button(control_frame, text="Home", command=turtle_home, padx=31, pady=7)
clear_button = Button(control_frame, text="Clear", command=turtle_clear, padx=31, pady=7)

# Turtle Config
turtle_config = ttk.Frame(control_frame)
turtle_shape_label = Label(turtle_config, text="Shape", padx = 45, pady=7)
shape_values = StringVar(value="turtle")
shape_list = ttk.Combobox(turtle_config, textvariable=shape_values)

# Place buttons on frame grid
forward_entry.grid(column=0, row=0, padx=15, pady=15)
forward_button.grid(column=1, row=0)
left_90_button.grid(column=0, row=1)
right_90_button.grid(column=1, row=1)

home_button.grid(column=0, row=2)
clear_button.grid(column=1, row=2)

turtle_config.grid(row=3, columnspan=2,  pady=31)
shape_list.grid(column=0, row=3)
turtle_shape_label.grid(column=1, row=3)

def change_shape(e):
  new_shape = shape_list.get()
  print("New shape " +new_shape)
  turtle1.shape(new_shape)
  # turtle1
  return

shape_list.bind('<<ComboboxSelected>>', lambda x: change_shape(x))
shape_list['values']= ('arrow', 'circle', 'turtle',  'square', 'triangle', 'classic')

turtle1.fd(100)
turtle1.left(90)
turtle1.fd(175)
turtle1.home()
turtle1.right(90)

root.mainloop()
