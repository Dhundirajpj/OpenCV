import cv2
import numpy as np
img=np.zeros((600,600,3),np.uint8) #Black Image
# print(img)
# img[:]= 255,0,0  #Blue Image
# img[200:300]=255,0,0
# img[:,200:300]=255,0,0
# cv2.rectangle(img,(0,0),(350,350),(255,0,0),2)
cv2.line(img,(0,0),(300,300),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED) #Filled Rectangle
cv2.circle(img,(400,50),30,(255,255,255),cv2.FILLED)
cv2.putText(img,"Dhundiraj",(300,150),cv2.FONT_ITALIC,2,(0,150,0),3)
cv2.imshow("Image",img)
cv2.waitKey(0)