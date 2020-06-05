# -*- coding: utf-8 -*-

D = {}
D['name'] = str(input("Enter your name: "))
D['surname'] = str(input("Enter your surname: "))
D['age'] = int(input("Enter your age: "))
D['height'] = float(input("Enter your height: "))
print("len(D['name']) = " + str(len(D['name'])))
print("len(D['surname']) = " + str(len(D['surname'])))
print(D.keys())
print(D.values())