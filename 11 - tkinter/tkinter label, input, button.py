# -*- coding: utf-8 -*-
#import tkinter
from tkinter import *

root = Tk()

# Text Labels
myLabel1 = Label(root, text="Hello, world!")
myLabel2 = Label(root, text="My name is:")
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 0)

# Input field
inputfield = Entry(root, width = 50, borderwidth = 5)
inputfield.grid(row = 2, column = 0)
inputfield.insert(0, "What's your name?")
# Button 
def myClick():
    myLabel3 = Label(root, text = " ")
    myLabel3.grid(row = 4, column = 0)
    hello = "Hello, " + inputfield.get()
    myLabel3 = Label(root, text = hello)
    myLabel3.grid(row = 4, column = 0)

myButton = Button(root, text = "Click here", command = myClick, fg = "blue", bg = "red")
myButton.grid(row = 3, column = 0)








root.mainloop()