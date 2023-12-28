#!/usr/bin/python
import os
from tkinter import *
import tkinter as tk
from tkinter import ttk
import turtle
from console import Console

root = Tk()
# root.config(background="red")
root.title("Tour The Turtle")

# Setting icon
try:
  relative_path = 'images/logos/current-logo.png'
  absolute_path = os.path.dirname(__file__)
  full_path = os.path.join(absolute_path, relative_path)
  img = PhotoImage(file=full_path)
  root.tk.call('wm', 'iconphoto', root._w, img)
except:
  print('Could not set icon image')

root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=4)
root.rowconfigure(2, weight=1)

top_bar = ttk.Frame(root, relief="raised")
top_bar.grid(row=0, column=0, columnspan=2, padx=5, sticky=W)
toggle_frame = LabelFrame(top_bar, text="Toggle", padx=15, pady=11)
# Initialize turtle with canvas section
turtleCanvas = turtle.ScrolledCanvas(root)
turtleCanvas.grid(column=0, row=1, rowspan=1, columnspan=1, sticky=(N, W, E, S))
global turtle1, turtle2, turtle3, turtle4, turtle5
global t1, t2, t3, t4, t5
global current_turtle
global settings_hidden, console_hidden
settings_hidden = False
console_hidden = False

# Initialize functions for turtle
def turtle_move():
  distance = int(distance_entry.get())
  direction = move_direction.get()
  if direction == 'forward':
    current_turtle.forward(distance)
  else:
    current_turtle.backward(distance)

def turtle_turn():
  angle = int(angle_entry.get())
  direction = direction_list.get()
  if(direction == 'right'):
    current_turtle.right(angle)
  else:
    current_turtle.left(angle)

turtle1 = turtle.RawTurtle(turtleCanvas)
current_turtle = t1 = turtle1
current_turtle.shape('turtle')
settings_frame = LabelFrame(root, text="Settings")
console_frame = ttk.Frame(root)

# Define all buttons to add to control frame
# Movement
movement_frame = LabelFrame(settings_frame, text="Move", padx=5, pady=7)
distance_entry = Entry(movement_frame, width=7)
distance_entry.insert(0, "55")
move_direction_values = StringVar(value="forward")
move_direction = ttk.Combobox(movement_frame, textvariable=move_direction_values, width=9)
move_direction['values'] = ('forward', 'backward')
move_button = Button(movement_frame, text="Move", command=turtle_move, padx=5, pady=7)
# pos_label = Label(movement_frame, text="Position")

def get_xcor():
  x = f'{current_turtle.xcor():.2f}'
  x_cor_entry.delete(0, END)
  x_cor_entry.insert(0, x)

def set_xcor():
  x = float(x_cor_entry.get())
  current_turtle.setx(x)

def get_ycor():
  y = f'{current_turtle.ycor():.2f}'
  y_cor_entry.delete(0, END)
  y_cor_entry.insert(0, y)

def set_ycor():
  y = float(y_cor_entry.get())
  current_turtle.sety(y)

x_cor_button = Button(movement_frame, text="xcor", command=get_xcor, pady=5, padx=5)
y_cor_button = Button(movement_frame, text="ycor", command=get_ycor, pady=5, padx=5)
x_cor_button.grid(row=2, column=0)
y_cor_button.grid(row=3, column=0)
x_cor_entry = Entry(movement_frame, width=7)
x_cor_entry.insert(0, current_turtle.xcor())
y_cor_entry = Entry(movement_frame, width=7)
y_cor_entry.insert(0, current_turtle.ycor())
x_cor_entry.grid(row=2, column=1)
y_cor_entry.grid(row=3, column=1)
setx_button = Button(movement_frame, text="Set X", command=set_xcor, pady=5, padx=5)
sety_button = Button(movement_frame, text="Set Y", command=set_ycor, pady=5, padx=5)
setx_button.grid(row=2, column=2)
sety_button.grid(row=3, column=2)

pos_values = Label(movement_frame, text="(0.00, 0.00)", border=2, borderwidth=1, relief="sunken", pady=5, padx=5)
def update_position():
  x,y = current_turtle.pos()
  x = f'{x:.2f}'
  y = f'{y:.2f}'
  current_position = '('+x+', '+ y+')'
  pos_values['text']= current_position

update_position = Button(movement_frame, text="Position",command=update_position)
# pos_label.grid(row=1, column=0)
pos_values.grid(row=4, column=1)
update_position.grid(row=4, column=0, padx=7)

# Layout movement frame as well as elements within movement frame
movement_frame.grid(row=0, column=0, padx=15, sticky=N)
move_direction.grid(row=0, column=0, pady=5, padx=15)
distance_entry.grid(row=0, column=1, padx=13, pady=15)
move_button.grid(row=0, column=2, padx=5, sticky=W+E)

# v_spacer1=Label(settings_frame, text="", height=1)
# v_spacer1.grid(row=1, column=0)

# Turn Frame with elements
turn_frame = LabelFrame(settings_frame, text="Turn", padx=11, pady=7)
angle_entry = Entry(turn_frame, width=3, borderwidth=3)
angle_entry.insert(0, "45")
direction_values = StringVar(value="right")
direction_list = ttk.Combobox(turn_frame, textvariable=direction_values, width=5)
direction_list['values'] = ('right', 'left')
turn_button = Button(turn_frame, text="Turn", command=turtle_turn, padx=19, pady=7)
# Layout Turn frame as well as elements within turn_frame
turn_frame.grid(row=1, column=0, pady=11)
direction_list.grid(row=0, column=0, padx=15)
angle_entry.grid(row=0, column=1, padx=31)
turn_button.grid(row=0, column=2, sticky=E, padx=17)

curves_frame = LabelFrame(settings_frame, text="Curves", padx=11, pady=7)
radius_entry = Entry(curves_frame, width=3, borderwidth=3)
radius_entry.insert(0, "15")

def draw_circle():
  radius = float(radius_entry.get())
  current_turtle.circle(radius=radius)

circle_button = Button(curves_frame, text="Circle", command=draw_circle)
curves_frame.grid(row=2, column=0)
radius_entry.grid(row=0, column=0)
circle_button.grid(row=0, column=1, padx=7)

def change_shape_visibility(e):
  visibility = shape_visibility_list.get()
  if visibility == 'showturtle':
    current_turtle.showturtle()
  else:
    current_turtle.hideturtle()

# Turtle Styling
style_frame = LabelFrame(settings_frame, text="Style", padx=9, pady=3)
style_frame.grid(row=3, column=0, columnspan=3)
shape_frame = LabelFrame(style_frame, text="Shape", padx=15, pady=5)
# turtle_shape_label = Label(style_frame, text="Shape", padx=1, pady=5)
shape_values = StringVar(value="turtle")
shape_list = ttk.Combobox(shape_frame, textvariable=shape_values, width=9)
shape_list.bind('<<ComboboxSelected>>', lambda x: change_shape(x))
shape_list['values']= ('arrow', 'circle', 'turtle',  'square', 'triangle', 'classic')
turtle_shape_stamp = Button(shape_frame, text="Stamp", padx=5, pady=5, command=current_turtle.stamp)
shape_visibility_values = StringVar(value="showturtle")
shape_visibility_list = ttk.Combobox(shape_frame, textvariable=shape_visibility_values, width=9)
shape_visibility_list.bind('<<ComboboxSelected>>', lambda x: change_shape_visibility(x))
shape_visibility_list['values']= ('showturtle', 'hideturtle')

# Shape Frame Layout
shape_frame.grid(column=0, row=0, columnspan=3, sticky=W+E, pady=5)
shape_list.grid(column=0, row=0)
shape_visibility_list.grid(column=1, row=0, padx=7)
turtle_shape_stamp.grid(column=2, row=0, padx=5)

def set_pen_size():
  p_size = int(pen_size_entry.get())
  current_turtle.pensize(p_size)

pen_frame = LabelFrame(style_frame, text="Pen")
pen_frame.grid(row=1, column=2, rowspan=5, padx=5, pady=17)
turtle_pen_size = Button(pen_frame, text="Set Pen", padx =15, pady=5, command=set_pen_size)
pen_values = StringVar(value="pendown")
pen_list = ttk.Combobox(pen_frame, textvariable=pen_values, width=9)
pen_list.bind('<<ComboboxSelected>>', lambda x: pen_state(x))
pen_list['values']= ('penup', 'pendown')
pen_size_entry = Entry(pen_frame, width=3, borderwidth=3)
pen_size_entry.insert(0, "1")
turtle_pen_size.grid(column=0, row=3, pady=5)
pen_size_entry.grid(column=0, row=2, pady=7)
pen_list.grid(column=0, row=1, pady=7, padx=7)

global filling
filling = False

def start_fill():
  current_turtle.begin_fill()
  fill_buttons(DISABLED, NORMAL)

def end_fill():
  current_turtle.end_fill()
  fill_buttons(ACTIVE, DISABLED)

def fill_buttons(begin_state, end_state):
  begin_fill_button = Button(style_frame, text="Begin Fill", state=begin_state, padx=3, pady=3, command=start_fill)
  end_fill_button  = Button(style_frame, text="End Fill", state=end_state, padx=3, pady=3, command=end_fill)
  begin_fill_button.grid(row=3, column=0)
  end_fill_button.grid(row=3, column=1)

def set_color(e):
  color_selected=simple_color_list.get()
  current_turtle.color(color_selected)

def set_pen_color(e):
  pen_color_selected=pen_color_list.get()
  current_turtle.pencolor(pen_color_selected)

def set_fill_color(e):
  fill_color_selected=fill_color_list.get()
  current_turtle.fillcolor(fill_color_selected)

fill_buttons(NORMAL, DISABLED)

color_list = ['black', 'red', 'green', 'blue', 'gray', 'white']
pen_color_label = Label(pen_frame, text="Pen Color", pady=15)
pen_color_values = StringVar(value='black')
pen_color_list = ttk.Combobox(pen_frame, textvariable=pen_color_values, width=7)
pen_color_list.bind("<<ComboboxSelected>>", lambda x: set_pen_color(x))
pen_color_list['values'] = color_list
# color_values.grid(row=5, column=0)
# pen_color_label.grid(row=4, column=0)
pen_color_list.grid(row=4, column=0, pady=7)

simple_color_label = Label(style_frame, text="Color", pady=15)
simple_color_values = StringVar(value='black')
simple_color_list = ttk.Combobox(style_frame, textvariable=simple_color_values, width=7)
simple_color_list.bind("<<ComboboxSelected>>", lambda x: set_color(x))
simple_color_list['values'] = color_list
# color_values.grid(row=5, column=0)
simple_color_label.grid(row=1, column=0)
simple_color_list.grid(row=1, column=1)

fill_color_label = Label(style_frame, text="Fill Color", pady=15)
fill_color_values = StringVar(value='black')
fill_color_list = ttk.Combobox(style_frame, textvariable=fill_color_values, width=7)
fill_color_list.bind("<<ComboboxSelected>>", lambda x: set_fill_color(x))
fill_color_list['values'] = color_list
# color_values.grid(row=5, column=0)
fill_color_label.grid(row=2, column=0)
fill_color_list.grid(row=2, column=1)

misc_frame = LabelFrame(settings_frame, text="Miscellaneous", padx=9, pady=5)
pen_up_button = Button(misc_frame, text="Pen Up", command=current_turtle.up, padx=9, pady=5)
pen_down_button = Button(misc_frame, text="Pen Down", command=current_turtle.down, padx=5, pady=7)
home_button = Button(misc_frame, text="Home", command=current_turtle.home, padx=5, pady=7)
clear_button = Button(misc_frame, text="Clear", command=current_turtle.clear, padx=5, pady=7)
reset_button = Button(misc_frame, text="Reset", command=current_turtle.reset, padx=5, pady=7)

misc_frame.grid(row=4, column=0, padx=5, pady=5, sticky=W+E)

global undo_button
def define_place_undo():
  global undo_button
  undo_button = Button(misc_frame, text="Undo", command=define_place_undo, padx=5, pady=7)
  undo_button.grid(column=1, row=0, sticky=W+E, padx=9, pady=3)
  if not current_turtle.undobufferentries():
    undo_button['state'] = DISABLED

pen_up_button.grid(column=0, columnspan=1, row=0, sticky=W+E, padx=9, pady=3)
define_place_undo()
clear_button.grid(column=2, row=0, sticky=W+E, padx=9, pady=3)
pen_down_button.grid(column=0, row=1, sticky=W+E, padx=9, pady=3)
home_button.grid(column=1, row=1, sticky=W+E, padx=9, pady=3)
reset_button.grid(column=2, columnspan=1, row=1, sticky=W+E, padx=9, pady=3)

def toggle_settings():
  global settings_hidden
  # First, toggle value
  settings_hidden = not settings_hidden
  if settings_hidden:
    settings_frame.grid_forget()
    settings_button.text = "Show Settings"
    root.columnconfigure(1, weight=0)
  else:
    settings_frame_show()
    settings_button.text = "Hide Settings"

def toggle_console():
  global console_hidden
  # First, toggle value
  console_hidden = not console_hidden
  if console_hidden:
    console_frame.grid_forget()
  else:
    console_frame.grid(row=2, column=0, columnspan=1, sticky=W+E)

toggle_frame.pack(fill=BOTH, expand=True)
settings_button = Button(toggle_frame, text="Settings", command=toggle_settings)
settings_button.grid(row=0, column=0)
spacer = Label(toggle_frame, text="")
spacer.grid(row=0, column=1, padx=15)
console_button = Button(toggle_frame, text="Console", command=toggle_console)
console_button.grid(row=0, column=2)

def settings_frame_show():
  settings_frame.grid(row=1, column=1, rowspan=2, columnspan=3, padx=15, pady=17, sticky=N)

# Lay the frames out appropriately
settings_frame_show()
console_frame.grid(row=2, column=0, columnspan=1, sticky=W+E)
console = Console(console_frame, locals(), root.destroy)
console.pack(fill=BOTH, expand=True)

def change_shape(e):
  new_shape = shape_list.get()
  current_turtle.shape(new_shape)

def pen_state(e):
  pen_state = pen_list.get()
  if pen_state == "penup":
    current_turtle.penup()
  else:
    current_turtle.pendown()

root.mainloop()