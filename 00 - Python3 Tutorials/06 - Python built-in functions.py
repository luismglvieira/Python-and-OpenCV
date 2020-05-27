#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:30:32 2020

@author: akaza
"""
x = 2
y = 4
a = x ** y
print("{0} ** {1} = {2}".format(x,y,a))
a = pow(x,y)
b = str("pow({0},{1}) = {2}".format(x,y,a))
print(b)
print(len(b)) #length of string
#
import math
c = math.sqrt(2)
print(c)