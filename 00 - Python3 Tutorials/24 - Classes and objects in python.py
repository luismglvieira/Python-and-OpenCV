# -*- coding: utf-8 -*-

class car:
    pass #empty class

ford = car()
honda = car()
volvo = car()
nissan = car()

ford.speed = 200
honda.speed = 180
volvo.speed = 190
nissan.speed = 220

ford.color = 'blue'
honda.color = 'white'
volvo.color = 'gray'
nissan.color = 'black'

print(str(ford.speed) + " " + str(ford.color))

ford.speed = 220
ford.color = 'green'

print(str(ford.speed) + " " + str(ford.color))