# -*- coding: utf-8 -*-

class car:
    def __init__(self, speed, color):
        self.__speed = speed    # double underscore
        self.__color = color        # means private
    
    def set_speed(self,value):
        self.__speed = value   
    def get_speed(self):            
        return self.__speed
    
    def set_color(self, value):
        self.__color = value
    def get_color(self):
        return self.__color
        
    
ford = car(200, 'blue')
honda = car(180, 'white')
volvo = car(190, 'gray')
nissan = car(220, 'black')

print('Old Ford speed = ' + str(ford.get_speed()))
print('Old Ford color = ' + str(ford.get_color()))

ford.set_speed(300)
ford.set_color('red')

print('New Ford speed = ' + str(ford.get_speed()))
print('New Ford color = ' + str(ford.get_color()))
print()
####

class rectangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        
    def set_height(self, height):
        self.__height = height
    def get_height(self):
        return self.__height
    
    def set_width(self, width):
         self.__width = width
    def get_width(self):
        return self.__width    
    
    def area(self):
        return self.__height * self.__width
        
rect1 = rectangle(20,60)
rect2 = rectangle(50,40)

print("Old rect1.area = " + str(rect1.area()))
print("Old rect2.area = " + str(rect2.area()))

rect1.set_height(40)
rect2.set_width(100)

print("New rect1.area = " + str(rect1.area()))
print("New rect2.area = " + str(rect2.area()))



