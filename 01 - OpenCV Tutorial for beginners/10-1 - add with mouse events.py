import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        img[y:y+60,x:x+60] = ball
        cv2.imshow('image', img)

img = cv2.imread('10 - messi5.jpg')
ball = img[280:340,330:390]

cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()