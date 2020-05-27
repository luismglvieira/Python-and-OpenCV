# -*- coding: utf-8 -*-

x = [3,5,4,9,7,10]
print(x)

for i in range(0,len(x)):
    print("The value at index " + str(i) + " is " + str(x[i]))
    
for i in range(0,len(x)):

    x.insert(i,i)   # insert new element to the left
    x.pop()         # remove last element

print(x)

x.clear()

print(x)

x = [9,2,5,4,3]
print(x)
x.sort()
print(x)
x.reverse()
print(x)
x.append(2)
print(x)
num = x.count(2)
print(num)