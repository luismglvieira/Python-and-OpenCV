# -*- coding: utf-8 -*-
# From https://www.youtube.com/watch?v=F5PfbC5ld-Q

from tkinter import *

root = Tk()
root.title("Simple calculator")

entrada = Entry(root, width=35, borderwidth=5)
entrada.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = entrada.get()
    entrada.delete(0, END)
    entrada.insert(0, str(current) + str(number))
    
def button_clear():
    entrada.delete(0, END)
    
def button_equal():
    num2 = entrada.get()
    entrada.delete(0, END) 
    if math == "addition":
        entrada.insert(0,f_num + int(num2))
    if math == "subtraction":
        entrada.insert(0,f_num - float(num2))
    if math == "division":
        entrada.insert(0,f_num / float(num2))    
    if math == "multiplication":
        entrada.insert(0,f_num * float(num2))     

def button_add():
    num1 = entrada.get()
    global f_num
    global math
    math = "addition"
    f_num = float(num1)
    entrada.delete(0, END)
    
def button_sub():
    num1 = entrada.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(num1)
    entrada.delete(0, END)
    
def button_div():
    num1 = entrada.get()
    global f_num
    global math
    math = "division"
    f_num = float(num1)
    entrada.delete(0, END)
    
def button_mlt():
    num1 = entrada.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(num1)
    entrada.delete(0, END)

 
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))

button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_equ = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clr = Button(root, text="c", padx=93, pady=20, command=button_clear)

button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_sub = Button(root, text="-", padx=41, pady=20, command=button_sub)
button_div = Button(root, text="/", padx=41, pady=20, command=button_div)
button_mlt = Button(root, text="x", padx=41, pady=20, command=button_mlt)



button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_equ.grid(row=5,column=1, columnspan=2)
button_clr.grid(row=4,column=1, columnspan=2)

button_add.grid(row=5,column=0)
button_sub.grid(row=6,column=0)
button_div.grid(row=6,column=2)
button_mlt.grid(row=6,column=1)

root.mainloop()