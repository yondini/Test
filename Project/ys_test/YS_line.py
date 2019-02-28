import cv2
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
import os, sys

cam=cv2.VideoCapture("line.mp4")
time.sleep(2)

fit_result, l_fit_result, r_fit_result, L_lane,R_lane = [], [], [], [], []


def Collect_points(lines):

    # reshape [:4] to [:2]
    interp = lines.reshape(lines.shape[0]*2,2)
    # interpolation & collecting points for RANSAC
    for line in lines:
        if np.abs(line[3]-line[1]) > 5:
            tmp = np.abs(line[3]-line[1])
            a = line[0] ; b = line[1] ; c = line[2] ; d = line[3]
            slope = (line[2]-line[0])/(line[3]-line[1]) 
            for m in range(0,tmp,5):
                if slope>0:
                    new_point = np.array([[int(a+m*slope),int(b+m)]])
                    interp = np.concatenate((interp,new_point),axis = 0)
                elif slope<0:
                    new_point = np.array([[int(a-m*slope),int(b-m)]])
                    interp = np.concatenate((interp,new_point),axis = 0)                
    return interp

def ransac_line_fitting(img, lines, min=100):
    global fit_result, l_fit_result, r_fit_result
    best_line = np.array([0,0,0])
    if(len(lines)!=0):                
        for i in range(30):           
            sample = get_random_samples(lines)
            parameter = compute_model_parameter(sample)
            cost = model_verification(parameter, lines)                        
            if cost < min: # update best_line
                min = cost
                best_line = parameter
            if min < 3: break
        # erase outliers based on best line
        filtered_lines = erase_outliers(best_line, lines)
        fit_result = get_fitline(img, filtered_lines)
    else:
        if (fit_result[2]-fit_result[1])/(fit_result[1]-fit_result[0]) < 0:
            l_fit_result = fit_result
            return l_fit_result
        else:
            r_fit_result = fit_result
            return r_fit_result

    if (fit_result[2]-fit_result[1])/(fit_result[1]-fit_result[0]) < 0:
        l_fit_result = fit_result
        return l_fit_result
    else:
        r_fit_result = fit_result
        return r_fit_result

def smoothing(lines, pre_frame):
    # collect frames & print average line
    lines = np.squeeze(lines)
    avg_line = np.array([0,0,0,0])
    
    for ii,line in enumerate(reversed(lines)):
        if ii == pre_frame:
            break
        avg_line += line
    avg_line = avg_line / pre_frame

    return avg_line

def draw_lines(img, lines, color=[255, 0, 0], thickness=10):
    """
    NOTE: this is the function you might want to use as a starting point once you want to 
    average/extrapolate the line segments you detect to map out the full
    extent of the lane (going from the result shown in raw-lines-example.mp4
    to that shown in P1_example.mp4).  
    
    Think about things like separating line segments by their 
    slope ((y2-y1)/(x2-x1)) to decide which segments are part of the left
    line vs. the right line.  Then, you can average the position of each of 
    the lines and extrapolate to the top and bottom of the lane.
    
    This function draws `lines` with `color` and `thickness`.    
    Lines are drawn on the image inplace (mutates the image).
    If you want to make the lines semi-transparent, think about combining
    this function with the weighted_img() function below
    """
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

while True:
    fet, img = cam.read()
    img = cv2.resize(img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
    img_original = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(gray,7,100,100)
    edges = cv2.Canny(blur,50,150,apertureSize=3)
    lines = cv2.HoughLines(edges,1,np.pi/180,70)
    line_arr = np.squeeze(lines)
    slope_degree = (np.arctan2(line_arr[:,1] - line_arr[:,3], line_arr[:,0] - line_arr[:,2]) * 180) / np.pi
    L_lines, R_lines = line_arr[(slope_degree>0),:], line_arr[(slope_degree<0),:]
    L_interp = Collect_points(L_lines)
    R_interp = Collect_points(R_lines)
    left_fit_line = ransac_line_fitting(img, L_interp)
    right_fit_line = ransac_line_fitting(img, R_interp)

    L_lane.append(left_fit_line), R_lane.append(right_fit_line)
    left_fit_line = smoothing(L_lane, 10)    
    right_fit_line = smoothing(R_lane, 10)
    final = draw_fitline(img, left_fit_line, right_fit_line)

    try:
        rho=resultline[0]
        theta=resultline[1]
        print("rho:", rho)
        print("theta:", theta)
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0+1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 -1000*(a))

        #cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
        #cv2.line(img, cv2.GetSize(img),(0,0,255), 2)
        #cv2.line(img, lines,(0,0,255), 2)

        
    except:
        print("can't find line")
    res = np.vstack((img_original,img))
    if cv2.waitKey(1)&0xFF == ord('q'):
        break
    cv2.imshow('img',res)
    
cv2.destroyAllWindows()
