import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import random
import os, sys

cap=cv2.VideoCapture('line_640x480.mp4')
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

def draw_fitline(img, result_l,result_r, color=(255,0,255), thickness = 10):
    # draw fitting line
    lane = np.zeros_like(img)
    cv2.line(lane, (int(result_l[0]) , int(result_l[1])), (int(result_l[2]), int(result_l[3])), color, thickness)
    cv2.line(lane, (int(result_r[0]) , int(result_r[1])), (int(result_r[2]), int(result_r[3])), color, thickness)
    # add original image & extracted lane lines
    final = weighted_img(lane, img, 1,0.5)  
    return final

while True:
    ret, frame = cap.read()
    height, width = frame.shape[:2]
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #blur = cv2.GaussianBlur(gray,(3, 3), 0)
    blur = cv2.bilateralFilter(gray,7,100,100)
    edges = cv2.Canny(blur,120,200,apertureSize=3)    
    lines = cv2.HoughLinesP(edges, 1, 1 * np.pi/180, 50, np.array([]), minLineLength=10, maxLineGap=20)

    try:
        line_arr = np.squeeze(lines)
        slope_degree = (np.arctan2(line_arr[:,1] - line_arr[:,3], line_arr[:,0] - line_arr[:,2]) * 180) / np.pi
        
        line_arr = line_arr[np.abs(slope_degree)<160]
        slope_degree = slope_degree[np.abs(slope_degree)<160]

        line_arr = line_arr[np.abs(slope_degree)>95]
        slope_degree = slope_degree[np.abs(slope_degree)>95]
        L_lines, R_lines = line_arr[(slope_degree>0),:], line_arr[(slope_degree<0),:]

        L_interp = Collect_points(L_lines)
        R_interp = Collect_points(R_lines)

        left_fit_line = ransac_line_fitting(frame, L_interp)
        right_fit_line = ransac_line_fitting(frame, R_interp)

        L_lane.append(left_fit_line), R_lane.append(right_fit_line)

        if len(L_lane) > 10:
            left_fit_line = smoothing(L_lane, 10)
        if len(R_lane) > 10:
            right_fit_line = smoothing(R_lane, 10)

        final = draw_fitline(frame, left_fit_line, right_fit_line)
    except:
        print("can't find lines")

    cv2.imshow('result',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
