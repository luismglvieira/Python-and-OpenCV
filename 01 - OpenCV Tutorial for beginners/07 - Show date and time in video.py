import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# cap.set(3, 320)
# cap.set(4, 240)
# print(cap.get(3))
# print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        fnt = cv2.FONT_HERSHEY_SIMPLEX
        txt = 'width: '+ str(cap.get(3)) + ' height: ' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (300,50), fnt, .5,
                            (0,255,255), 1, cv2.LINE_AA)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()