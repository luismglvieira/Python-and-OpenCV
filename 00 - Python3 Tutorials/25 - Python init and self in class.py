# -*- coding: utf-8 -*-

class car:
    def __init__(self, speed, color):
        print('the function __init__ is called' )
        print(speed)
        print(color)
        self.speed = speed
        self.color = color
          
ford = car(200, 'blue')
honda = car(180, 'white')
volvo = car(190, 'gray')
nissan = car(220, 'black')
print()
print("old Ford was " + str(ford.speed) + " " + str(ford.color))

ford.speed = 220
ford.color = 'green'
print("new Ford is " + str(ford.speed) + " " + str(ford.color))
print()
##

class rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.area = height*width
        
rect1 = rectangle(20,60)
rect2 = rectangle(50,40)

print("rect1.area = " + str(rect1.area))
print("rect2.area = " + str(rect2.area))