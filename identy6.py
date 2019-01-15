import numpy as np
import cv2

img = cv2.imread("file.jpg",-1)

#assuming bounding boxes are given as tuples bb1,bb2,bb3,bb4
#Use numpy indexing to crop out bounding boxes from img
#use np.hstack and np.vstack to arrange them in 2x2 matrix fashion.
#cv2.imwrite() will save the file
