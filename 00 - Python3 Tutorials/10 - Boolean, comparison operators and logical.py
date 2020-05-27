# -*- coding: utf-8 -*-

print("10 < 9 is " + str(10 < 9))
print("10 > 9 is " + str(10 > 9))
print("10 == 10 is " + str(10 == 10))
print("10 != 11 is " + str(10 != 11))

x = 20
y = 30
a = x >= y
print("{0} > = {1} is {2}".format(x,y,a))

x = 40
y = 30
a = x >= y
print("{0} > = {1} is {2}".format(x,y,a))

x = "hello"
y = "world"
a = x == y
print("{0} == {1} is {2}".format(x,y,a))

x = "hello"
y = "Hello"
a = x == y
print("{0} == {1} is {2}".format(x,y,a))

a = x == y.lower()
print("{0} == {1} is {2}".format(x,y.lower(),a))

x = 30
y = 20
z = 10
a = x > y
b = y < z
c = a and b
print ("{0} > {1} and {1} < {2} is {3}".format(x,y,z,c))
c = a or b
print ("{0} > {1} or {1} < {2} is {3}".format(x,y,z,c))



