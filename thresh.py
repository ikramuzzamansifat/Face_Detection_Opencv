import cv2 as cv 
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img) 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
cv.imshow('Gray', gray) 

# Thresholding is a binary realisation of an image. 
# In general, we want to take an image & convert it to a binary image, 
#  that's an image where pixels are either zero/black, or 255/white
#  Example of thresholding: take an image, & take some particular value that we're going to call 
#  the thresholding value & compare each pixel of the image to this threshold value . 
#  Either intensity is < the threshold value, we set the pixel intensity = 0, and 
#  if > the threshold value, set it to 255


#  Simple thresholding 
#  thresh  is the thresholded image/binirized image, 
#  threshold, is essentially the same value that we passed 150, the same 
# same threshold value we pass in, will be returned to this threshold value. 
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Downsides of Simple thresholding: 
#           We have to manually specify a specific threshold value. 
#   Some cases, it might work, but in advanced cases, it won't. 
#  so, we could do let the computer find the optimal threshold value itself. 

#adaptive method tells machine which method to use when computing the optimal threshold 
#  value  

#  Adaptive Thresholding 
adaptive_thresh = cv.adaptiveThreshold(gray, 255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11,9)
cv.imshow('Adapting thresholding', adaptive_thresh)

cv.waitKey(0) 