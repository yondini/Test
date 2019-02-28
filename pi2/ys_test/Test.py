import cv2
import numpy as np
import time

cam=cv2.VideoCapture('line.mp4')
time.sleep(2)

def Point_L(img, rho, theta):
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0+1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 -1000*(a))

    return cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

def Point_R(img, rho, theta):
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0+1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 -1000*(a))

    return cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)

L_line = []
R_line = []

while True:
    fet, img = cam.read()
    img = cv2.resize(img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
    img_original = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(gray,7,100,100)
    edges = cv2.Canny(blur,120,200,apertureSize=3)
    lines = cv2.HoughLines(edges,1,np.pi/180,130)

    Left = []
    Right = []
    result_L = [1000]*2
    result_R = [0]*2

    if len(lines)!=0:
        for i in range(len(lines)):
            if lines[i][0][0]>0:
                Left.append(lines[i])
            else:
                Right.append(lines[i])

    else:
        



    cv2.imshow('img',img)
    
cv2.destroyAllWindows()
