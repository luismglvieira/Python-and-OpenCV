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
    
#    if event == cv2.EVENT_MOUSEMOVE:
#        mousePosX = x
#        mousePosY = y
#        print('(' + str(x) + ',' + str(y) + ')')
    if event == cv2.EVENT_LBUTTONDOWN:
        mouseClick = (x,y)
        leftClick = True
        print('leftClick = ' + str(leftClick) + ' at (' + str(x) + ',' + str(y) + ')')

    if event == cv2.EVENT_LBUTTONUP:
        mouseRelease = (x,y)
        leftClick = False
        print('leftClick = ' + str(leftClick) + ' at (' + str(x) + ',' + str(y) + ')')



cv2.namedWindow('image')
img = cv2.imread('10 - messi5.jpg')  
b,g,r = cv2.split(img)
img_copy = np.copy(img)

algorithms_list = [cv2.THRESH_BINARY,cv2.THRESH_BINARY_INV,cv2.THRESH_TRUNC,cv2.THRESH_TOZERO,cv2.THRESH_TOZERO_INV]

trackbar_list = [['threshold_B',0,300],    # ['Trackbar_Title',min,max]
                 ['max_binary_B',0,300],
                 ['thresh_alg_B',0,4],
                 ['threshold_G',0,300],
                 ['max_binary_G',0,300],
                 ['thresh_alg_G',0,4],
                 ['threshold_R',0,300],
                 ['max_binary_R',0,300],
                 ['thresh_alg_R',0,4]]

trackbar_pos = [0]*len(trackbar_list)       

for x in trackbar_list:
    cv2.createTrackbar(str(x[0]),'image',x[1],x[2],nothing)

while(1):
    b_copy = np.copy(b)
    g_copy = np.copy(g)
    r_copy = np.copy(r)
    
    for k in range(0,len(trackbar_list)):
        trackbar_pos[k] = cv2.getTrackbarPos(str(trackbar_list[k][0]),'image')

    _,b_copy = cv2.threshold(b_copy, trackbar_pos[0], trackbar_pos[1], trackbar_pos[2])
    _,g_copy = cv2.threshold(g_copy, trackbar_pos[3], trackbar_pos[4], trackbar_pos[5])
    _,r_copy = cv2.threshold(r_copy, trackbar_pos[6], trackbar_pos[7], trackbar_pos[8]) 
        
    #######################################################
        
    img_copy = cv2.merge((b_copy,g_copy,r_copy))
    
    cv2.imshow('image',img_copy)
    cv2.setMouseCallback('image',mouse_event)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    

cv2.destroyAllWindows()# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-

