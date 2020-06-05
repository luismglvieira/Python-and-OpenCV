# -*- coding: utf-8 -*-

a = [0,1,2,3,4,5]   #list
b = (0,1,2,3,4,5)   #tuple
c = {0,1,2,3,4,5}   #set
d = '013456'        #string
e = {               #dictionary
     "name": 'luis',
     "age": 27}

print("a:")
for x in a:
    print(x)
print()
print("b:")
for x in b:
    print(x)
print()
print("c:")
for x in c:
    print(x)
print()
print("e.keys():")
for x in e.keys():
    print(x)
print()    
print("e.values():")
for x in e.values():
    print(x)
print()
print("e.items():")
for x in e.items():
    print(x)
print()
print("range(5):")
for x in range(5):
    print(x)
print()
print("range(2,5):") 
for x in range(2,5):
    print(x)
print()
print("range(2,30,3):")
for x in range(2,30,3):
    print(x)
else:
    print("finished")