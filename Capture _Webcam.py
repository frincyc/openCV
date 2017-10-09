import cv2
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
capture = cv2.VideoCapture(0)
while(True):
    #Reading Frame
    ret,frame=capture.read()

    #Operations on Frame
    grayFrame= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Display Capture on Screen
    cv2.imshow("Black and White",grayFrame)
    filename=datetime.now().strftime("%Y%m%d-%H%M%S")

    #Save the capture to given location
    cv2.imwrite('Capture{0}.jpg'.format(filename), grayFrame)

    #Press Esc to Quit
    if cv2.waitKey(0) == 27:
        break;

#releasing capture
capture.release()
cv2.destroyAllWindows()
