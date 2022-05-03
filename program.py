import cv2
import time
import numpy as np

fourcc=cv2.VideoWriter_fourcc(*'XVID')
outputFile=cv2.VideoWriter('Output.avi',fourcc,20.0,(640,480))

cap=cv2.VideoCapture(0)

time.sleep(2)

bg=0

for i in range (60):
    ret,bg=cap.read()

bg=np.flip(bg,axis=1)

while (cap.isOpened()):
    ret,img=cap.read()
    if not ret:
        break
    img=np.flip(img,axis=1)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lower_red=np.array([68, 240, 86])
    upper_red=np.array([160, 81, 76])

    mask_1=cv2.inRange(hsv,lower_red,upper_red)

    lower_red=np.array([60, 40, 40])
    upper_red=np.array([130, 255, 255])

    mask_2=cv2.inRange(hsv,lower_red,upper_red)

    mask_1=mask_1+mask_2
    
    mask_1=cv2.morphologyEx(mask_1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask_1=cv2.morphologyEx(mask_1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))

    mask_2=cv2.bitwise_not(mask_1)

    res_1=cv2.bitwise_and(img,img,mask=mask_2)
    res_2=cv2.bitwise_and(bg,bg,mask=mask_1)

    final_Output=cv2.addWeighted(res_1,1,res_2,1,0)
    
    outputFile.write(final_Output)

    cv2.imshow('magic',final_Output)
    cv2.waitKey(1)

cap.release()
out.release()
cv2.destroyAllWindows()
