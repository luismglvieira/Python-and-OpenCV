# -*- coding: utf-8 -*-

def sumFunc(arg1,arg2):
    print(a,"+",b,"=",arg1 + arg2)

def multFunc(arg1,arg2):
    print(a,"*",b,"=",arg1 * arg2)


a = float(input("Insert first number: "))
b = float(input("Insert second number: "))
c = str(input("Type '*' for Multiplication or type '+' to addition: "))

if c == '*':
    multFunc(a,b)
elif c == '+':
    sumFunc(a,b)
else:
    print("Wrong operation.")
    