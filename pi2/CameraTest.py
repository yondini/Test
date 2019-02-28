import cv2
 
cam = cv2.VideoCapture(0)
width = 300
height = 200
cam.set(3,width) #CV_CAP_PROP_FRAME_WIDTH
cam.set(4,height) #CV_CAP_PROP_FRAME_HEIGHT
#cam.set(5,0) #CV_CAP_PROP_FPS
 
while True:
    ret_val, img = cv2.imread('slope_test.jpg') # 캠 이미지 불러오기
    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    for i in range(width):
        for j in range(height):
            if img[j,i,0] < 100 and img[j,i,1] < 100 and img[j,i,2]<100:
                img[j,i] = 0
            else:
                img[j,i]=255
    cv2.imshow("Cam Viewer",img) # 불러온 이미지 출력하기
    
    if cv2.waitKey(1) == 27:
        break  # esc to quit
 
