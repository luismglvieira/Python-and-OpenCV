# -*- coding: utf-8 -*-
import cv2
import numpy as np
def nothing(x):
    pass

mousePosX = 0
mousePosY = 0
mouseClick = ()
mouseRelease = ()
leftClick = False

def mouse_event(event, x, y, flags, param):
    global mousePos, mouseClick, mouseRelease, leftClick
    
    if event == cv2.EVENT_MOUSEMOVE:
        mousePosX = x
        mousePosY = y
#        print('(' + str(x) + ',' + str(y) + ')')
    if event == cv2.EVENT_LBUTTONDOWN:
#        mouseClick = (x,y)
        leftClick = True
#        print('leftClick = ' + str(leftClick) + ' at (' + str(x) + ',' + str(y) + ')')

    if event == cv2.EVENT_LBUTTONUP:
#        mouseRelease = (x,y)
        leftClick = False
#        print('leftClick = ' + str(leftClick) + ' at (' + str(x) + ',' + str(y) + ')')



cv2.namedWindow('image')
img = cv2.imread('10 - messi5.jpg')  
b,g,r = cv2.split(img)
img_copy = np.copy(img)

cv2.createTrackbar('threshold_value','image',0,300,nothing)
cv2.createTrackbar('max_binary_value','image',0,600,nothing)
#cv2.createTrackbar('R','image',0,600,nothing)

while(1):
    threshold_value = cv2.getTrackbarPos('threshold_value','image')
    max_binary_value = cv2.getTrackbarPos('max_binary_value','image')
#    r_pos = cv2.getTrackbarPos('R','image')
    b_copy = np.copy(b)

    _,img_copy = cv2.threshold(b_copy, threshold_value, max_binary_value, cv2.THRESH_BINARY )
    cv2.imshow('image',img_copy)
    cv2.setMouseCallback('image',mouse_event)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    

cv2.destroyAllWindows()# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-

