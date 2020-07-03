# -*- coding: utf-8 -*-

import cv2
import numpy as np
#import keyboard as kb

mousePos = ()
mouseClick = ()
mouseRelease = ()
leftClick = False

def mouse_event(event, x, y, flags, param):
    global mousePos, mouseClick, mouseRelease, leftClick
    
    if event == cv2.EVENT_MOUSEMOVE:
        mousePos = (x,y)
#        print('(' + str(x) + ',' + str(y) + ')')
    if event == cv2.EVENT_LBUTTONDOWN:
        mouseClick = (x,y)
        leftClick = True
        print('leftClick = ' + str(leftClick) + ' at (' + str(x) + ',' + str(y) + ')')

    if event == cv2.EVENT_LBUTTONUP:
        mouseRelease = (x,y)
        leftClick = False
        print('leftClick = ' + str(leftClick) + ' at (' + str(x) + ',' + str(y) + ')')
        
img1 = cv2.imread('10 - messi5.jpg')       

#cv2.imshow('image',img1)

 
#kb.press_and_release('shift+s, space')
#kb.write('The quick brown fox jumps over the lazy dog.')

cv2.imshow("img1",img1)
cv2.setMouseCallback('img1',mouse_event)    

cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.destroyAllWindows()# -*- coding: utf-8 -*- 