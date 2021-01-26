import cv2
import numpy as np
#Insert and show image
# img=cv2.imread("Resources/trip.jpg")
# cv2.imshow("Output",img)
# cv2.waitKey(0)

#Video
# cap=cv2.VideoCapture("Resources/v.mp4")
# while True:
#     success,img=cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

#Webcam
# cap=cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# while True:
#     success,img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break
kernel=np.ones((5,5),np.uint8)
img=cv2.imread("Resources/emma.jpeg")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(7,7),0)
imgCanny = cv2.Canny(img,150,200)
imgDilation =cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDilation,kernel,iterations=1)
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Original",img)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Canny Image",imgDilation)
cv2.imshow("Eroded Image",imgEroded)
# print(img.shape)
# print(imgGray.shape)

imgResize =cv2.resize(img,(112,200))
imgCropped =img[0:100,100:200]
cv2.imshow("Emma",imgResize)
cv2.imshow("Resized",img)
cv2.imshow("Cropped",imgCropped)
cv2.waitKey(0)