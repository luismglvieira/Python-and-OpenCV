# -*- coding: utf-8 -*-

x = 90
y = 100
if x == y:
    print(str(x) + " is equal to " + str(y))
else:
    print(str(x) + " isn\'t equal to " + str(y))

x = 80
y = 90
if x == y:
    print(str(x) + " is equal to " + str(y))
elif x > y:
    print(str(x) + " is greater than " + str(y))
else:
    print(str(x) + " is smaller than " + str(y))

x = -20
if x > 0:
    print(str(x) + " is positive.")
elif x < 0:
    print(str(x) + " is negative.")
else:
    print(str(x) + " is zero.")
    
x = -10
y = 0
if x > 0 and  y > 0:
    print(str(x) + " and " + str(y) + " are both positive.")
elif x == 0 or y == 0:
    print("Either " + str(x) + " or " + str(y) + " is zero.")
else:
    print("Either " + str(x) + " or " + str(y) + " is negative.")