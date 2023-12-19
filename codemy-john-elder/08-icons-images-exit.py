import os
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("The Turtle Tourer")
# # root.iconbitmap()
# if "nt" == os.name:
#     root.wm_iconbitmap(bitmap = "favicon.ico")
# else:
#     root.wm_iconbitmap(bitmap = "@favicon.xbm")

# https://stackoverflow.com/a/11180300/10645311
img = PhotoImage(file='images/current-icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)

# On Ubuntu, required to install the following package
# sudo apt-get install python3-pil python3-pil.imagetk
# See - https://stackoverflow.com/a/48170806/10645311

# import os
# unsplash_images = os.sy
my_img = ImageTk.PhotoImage(Image.open('images/unsplash/francesco-ungaro-turtle-small.jpg'))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
