import numpy as np
import cv2
capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out =  cv2.VideoWriter('Webcam_Output.avi',fourcc, 20.0,(1280,960))
while(capture.isOpened()):
    ret,frame=capture.read()
    if ret == True:
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey() == 27: #Press Esc key to exit recording
            break
    else:
        break
capture.release()
out.release()
cv2.destroyAllWindows()
