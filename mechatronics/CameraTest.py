import cv2
#import screeninfo

cam = cv2.VideoCapture(0)
width = 320
height = 240
cam.set(3,width) #CV_CAP_PROP_FRAME_WIDTH
cam.set(4,height) #CV_CAP_PROP_FRAME_HEIGHT
#cam.set(5,0) #CV_CAP_PROP_FPS

#screen = screeninfo.get_monitors()[2]

window_name = 'Cam Viewer'

#cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
#cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
#cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                          
#cv2.namedWindow(window_name,cv2.WINDOW_FULLSCREEN)
 
 
 
while True:
    ret_val, img = cam.read()
    binary = cv2.inRange(img,(
    
    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #for i in range(width):
    #    for j in range(height):
    #        if img[j,i,0] < 100 and img[j,i,1] < 100 and img[j,i,2]<100:
    #            img[j,i] = 0
    #        else:
    #            img[j,i]=255
    cv2.imshow("Cam Viewer",img)
    
    if cv2.waitKey(1) == 27:
        break  # esc to quit
 
