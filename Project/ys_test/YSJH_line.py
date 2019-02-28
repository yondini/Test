import cv2
import numpy as np
import time
cam=cv2.VideoCapture('line.mp4')
time.sleep(2)

while True:
    fet, img = cam.read()
    img = cv2.resize(img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
    img_original = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(gray,7,100,100)
    edges = cv2.Canny(blur,120,200,apertureSize=3)
    lines = cv2.HoughLines(edges,1,np.pi/180,130)

    for i in range(len(lines)):
        

    resultline=[0]*3        

    try:
        resultline=[0]*3  
        for i in range(len(lines)):
            if resultline[1]<lines[i][0][1]:
                resultline[0]=lines[i][0][0]
                resultline[1]=lines[i][0][1]

        rho=resultline[0]
        theta=resultline[1]
        #print(theta)
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0+1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 -1000*(a))
        """
        cv2.line(blur,(x1,y1),(x2,y2),(0,0,255),2)
        """
    except:
        print("can't find line")
    if cv2.waitKey(1)&0xFF == ord('q'):
        break
    cv2.imshow('img',img)
    
cv2.destroyAllWindows()
