# -*- coding: utf-8 -*-
# From https://www.youtube.com/watch?v=zg4c92pNFeo

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')

my_img1 = ImageTk.PhotoImage(Image.open("dir/kimmie.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("dir/polygon.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("dir/sunny.jpg"))

image_list = [my_img1, my_img2, my_img3]

img_index = 1
status_text = "Image " + str(img_index) + " of " + str(len(image_list))
status = Label(root, text=status_text)
status.grid(row=2,column=1)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)



def forward(img_index):
    global my_label
    global button_fwd
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[img_index-1])
    button_fwd = Button(root, text=">>", command=lambda: forward(img_index+1))
    button_back = Button(root,text="<<", command=lambda: back(img_index-1))
    
    if img_index==len(image_list):
        button_fwd = Button(root, text=">>", state=DISABLED)
    
    button_back.grid(row=1, column=0)
    button_fwd.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)
    
    status_text = "Image " + str(img_index) + " of " + str(len(image_list))
    status = Label(root, text=status_text)
    status.grid(row=2,column=1)
    
     
def back(img_index):
    global my_label
    global button_fwd
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[img_index-1])
    button_fwd = Button(root, text=">>", command=lambda: forward(img_index+1))
    button_back = Button(root,text="<<", command=lambda: back(img_index-1))
    
    if img_index==1:
        button_back = Button(root, text="<<", state=DISABLED)
    
    button_back.grid(row=1, column=0)
    button_fwd.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)
    
    status_text = "Image " + str(img_index) + " of " + str(len(image_list))
    status = Label(root, text=status_text)
    status.grid(row=2,column=1)
   
#############    INITIAL VARIABLES
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_fwd = Button(root, text=">>",command=lambda: forward(2))
button_exit = Button(root, text="Exit", command=root.quit)

button_back.grid(row=1, column=0)
button_fwd.grid(row=1, column=2)
button_exit.grid(row=1, column=1)

root.mainloop()