import cv2
import numpy as np
import time

cam=cv2.VideoCapture(0)
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
    lines = cv2.HoughLines(edges,1,np.pi/180,120)

    Left = []
    Right = []
    result_L = [1000]*2
    result_R = [0]*2

    try:
        for i in range(len(lines)):
            if lines[i][0][0]>0:
                Left.append(lines[i])
            elif lines[i][0][0]<0:
                Right.append(lines[i])
                
        if len(Left)!=0: 
            for i in range(len(Left)):
                if result_L[1]>Left[i][0][1]:
                    result_L[0]=Left[i][0][0]
                    result_L[1]=Left[i][0][1]
                    value_L = [result_L[0], result_L[1]]
                    
            print("Left:", value_L)
            
        if len(Right)!=0:
            for i in range(len(Right)):
                if result_R[1]<Right[i][0][1]:
                    result_R[0]=Right[i][0][0]
                    result_R[1]=Right[i][0][1]
                    value_R = [result_R[0], result_R[1]]
            print("Right:", value_R)

        if len(Left)==0 or len(Right)==0:
            if len(Left)==0:
                Point_R(img, result_R[0], result_R[1])
            if len(Right)==0:
                Point_L(img, result_L[0], result_L[1])
        else:
             Point_L(img, result_L[0], result_L[1])
             Point_R(img, result_R[0], result_R[1])
       
    except:
        print("can't find line")
        
    if cv2.waitKey(1)&0xFF == ord('q'):
        break
    
    cv2.imshow('img',img)
    
cv2.destroyAllWindows()

"""
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
    _left=0
    _right=0

  
    for i in range(len(lines)):
        if lines[i][0][0]>0:
            Left.append(lines[i])
        else:
        
            Right.append(lines[i])

    for i in range(len(Left)):
        if result_L[1]>Left[i][0][1]:
            result_L[0]=Left[i][0][0]
            result_L[1]=Left[i][0][1]
    for i in range(len(Right)):
        if result_R[1]<Right[i][0][1]:
            result_R[0]=Right[i][0][0]
            result_R[1]=Right[i][0][1]

    if len(Left)==0 or len(Right)==0:
        if len(Left)==0:
            Point_R(img, result_R[0], result_R[1])
        if len(Right)==0:
            Point_L(img, result_L[0], result_L[1])
    else:
         Point_L(img, result_L[0], result_L[1])
         Point_R(img, result_R[0], result_R[1])
        
    
    if cv2.waitKey(1)&0xFF == ord('q'):
        break
    
    cv2.imshow('img',img)
    
cv2.destroyAllWindows()
"""
"""
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

    for i in range(len(lines)):
        if lines[i][0][0]>0:
            Left.append(lines[i])
        else:
            Right.append(lines[i])
            
    for i in range(len(Left)):
        if result_L[1]>Left[i][0][1]:
            result_L[0]=Left[i][0][0]
            result_L[1]=Left[i][0][1]
    for i in range(len(Right)):
        if result_R[1]<Right[i][0][1]:
            result_R[0]=Right[i][0][0]
            result_R[1]=Right[i][0][1]

    if len(Left)==0 or len(Right)==0:
        if len(Left)==0:
            Point_R(img, result_R[0], result_R[1])
        if len(Right)==0:
            Point_L(img, result_L[0], result_L[1])
    else:
         Point_L(img, result_L[0], result_L[1])
         Point_R(img, result_R[0], result_R[1])
        
    
    if cv2.waitKey(1)&0xFF == ord('q'):
        break
    
    cv2.imshow('img',img)
    
cv2.destroyAllWindows()

"""    
"""
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

    try:
        for i in range(len(lines)):
            if lines[i][0][0]>0:
                Left.append(lines[i])
            else:
                Right.append(lines[i])
        print("Left:", Left[len(Left)-1])
        print("Right:", Right[len(Right)-1])
   
        for i in range(len(Left)):
            if result_L[1]>Left[i][0][1]:
                result_L[0]=Left[i][0][0]
                result_L[1]=Left[i][0][1]
        for i in range(len(Right)):
            if result_R[1]<Right[i][0][1]:
                result_R[0]=Right[i][0][0]
                result_R[1]=Right[i][0][1]
   
        print("left[",result_L[0],"][",result_L[1],"]")
        print("right[",result_R[0],"][",result_R[1],"]")

        Point_L(img, result_L[0], result_L[1])
        Point_R(img, result_R[0], result_R[1])
       
    except:
        print("can't find line")
    if cv2.waitKey(1)&0xFF == ord('q'):
        break
    
    cv2.imshow('img',img)
    
cv2.destroyAllWindows()
"""
