from curses.textpad import rectangle
import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype = 'uint8') 

rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1) # -1 for fill the image 
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1) 

cv.imshow('Rectangle: ',rectangle)
cv.imshow('Circle: ', circle)

# bitwise AND --> Intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle) 
cv.imshow('Bitwise and', bitwise_and)

# bitwise_and_ = cv.bitwise_and(circle, rectangle)
# cv.imshow('Bitwise and _ ', bitwise_and_) 

# Bitwise OR --> Intersecting region + non-intersecting regions 
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# Bitwise XOR --> non-intersecting regions 
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)


# bitwise NOT 
bitwise_not = cv.bitwise_not(circle) 
cv.imshow('Rectangle NOT', bitwise_not)

cv.waitKey(0) 


