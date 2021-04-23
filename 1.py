#Imported Library
import cv2

#added path
path = "Ai_Practical\images\lambo.jpg"

#Reading Image

Image = cv2.imread(path)
Image_C = cv2.Canny(Image,10,10)

#Displaying Image
cv2.imshow("1st",Image)
cv2.imshow("2nd",Image_C)

#Stopping from closing
cv2.waitKey(0)

