#  Edge detection

import cv2 as cv 
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Cats', img) 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
cv.imshow('Gray', gray) 

#  Laplacing method 
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap)) 
cv.imshow('Laplacian', lap) 

#  Sobel method 
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) 
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely) 

cv.imshow('Sobel x', sobelx)
cv.imshow('Sobel y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

# canny is a multi stage process, it uses sobel in one of it's stage to compute the gradients of the image....
canny = cv.Canny(gray, 150, 175) 
cv.imshow('Canny', canny) 
cv.waitKey(0) 