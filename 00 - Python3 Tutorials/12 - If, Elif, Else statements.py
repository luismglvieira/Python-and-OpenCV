# -*- coding: utf-8 -*-

x = int(input("Enter an integer number: "))

if x > 0:

    if (x%2) == 0:
        print("Your number, " + str(x) + ", is positive and even.")
    else:
        print("Your number, " + str(x) + ", is positive and odd.")
elif x == 0:
    print("Your number is zero.")
else:
    print("Your number, " + str(x) + ", is negative.")