import cv2 as cv 
import numpy as np

img = cv.imread('Photos/cats 2.jpg')
cv.imshow('Cats', img) 

blank = np.zeros((img.shape[:2]), dtype = 'uint8')
# blank = np.zeros((400, 400), dtype = 'uint8') 

cv.imshow('Blank image', blank) 

### Opencv masking essentially allows us to focus on certain parts of an image 
#  we'd like to focus on. 


circle = cv.circle(blank.copy(), (img.shape[1] // 2 + 45, img.shape[0]//2 ), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)  
# cv.rectangle() 
# cv.imshow('Mask', circle) 
# cv.imshow('Mask rect', rectangle)
# masked_circle = cv.bitwise_and(img, img, mask=circle)
# cv.imshow('Masked Image', masked_circle)
# masked_rectangle= cv.bitwise_and(img, img, mask = rectangle) 
# cv.imshow('Masked Rectangle Image', masked_rectangle)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird Shape', weird_shape) 

# Size of our mask has to be at the same dimensions as that of our image 
masked = cv.bitwise_and(img, img, mask = weird_shape)  
cv.imshow('Weird shaped Masked image', masked)


cv.waitKey(0) 