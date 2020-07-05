# -*- coding: utf-8 -*-

from tkinter import *
from PIL import ImageTk,Image
import cv2

root = Tk()
root.title('Learn to code')
#root.iconbitmap('recttransparente.ico') # não funciona

my_img = ImageTk.PhotoImage(Image.open("recttransparente.png"))
my_label = Label(image=my_img)
my_label.pack()


def button_quit():
    root.quit()
    cv2.destroyAllWindows()
    
button_quit = Button(root, text="Exit", command=button_quit)
button_quit.pack()

root.mainloop()

