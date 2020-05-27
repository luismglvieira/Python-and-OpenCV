import cv2

cap = cv2.VideoCapture(0)   # capture from default camera
# Video flags to capture properties
# https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("width", frame_width)
print("height", frame_height)

# Video write conditions
fourcc = cv2.VideoWriter_fourcc(*'XVID')
outColor = cv2.VideoWriter('04 - outColor.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):  # requires that cap variable 0 is set up correctly
    ret, frame = cap.read()     # read capture
    if ret == True:     # only happens if there's capture happening
        # show video capture on window "color frame"
        cv2.imshow('color frame',frame)

        # convert to grayscale and show on window "gray frame"
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray frame', grayFrame)

        # write "frame" using video settings "outColor"
        outColor.write(frame)

        # quit when key Q is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break # if there's no capture happening, breaks the loop

cap.release()   # free up capture resources
outColor.release() # free write resources
cv2.destroyAllWindows()
