# -*- coding: utf-8 -*-

a = range(0,10)
b = int(input("Insert number from 0 to 10 to stop the loop: "))

for x in a:
    if x == b:
        break
    print(x)

a = range(0,10)
b = int(input("Insert number from 0 to 10 to skip one step: "))

for x in a:
    if x == b:
        continue
    print(x)
    
a = range(0,10)
b = int(input("Insert number from 0 to 10 to skip while loop: "))
i = 0
while i < 10:
    i += 1
    if i == b:
        continue
    print(i)
    

