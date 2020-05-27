import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(x,', ', y)
        fnt = cv2.FONT_HERSHEY_SIMPLEX
        txtxy = ("("+ str(x) + ', ' + str(y) +")")
        cv2.putText(img, txtxy, (x, y), fnt, .6, (255,0,0), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_MBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        fnt = cv2.FONT_HERSHEY_SIMPLEX
        txtbgr = ("("+ str(blue) + ', ' + str(green) + ', ' + str(red) +")")
        cv2.putText(img, txtbgr, (x, y), fnt, .6, (int(blue), int(green), int(red)), 2)
        cv2.imshow('image', img)

img = cv2.imread('03 - lena_copy.png')
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()