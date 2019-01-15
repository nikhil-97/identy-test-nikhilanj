# NOTE :: Using Python 2, and OpenCV 2.4.9.1
import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filepath", help="Enter the absolute filepath")
args = parser.parse_args()

fp = args.filepath

img = cv2.imread(fp,-1)

h,w,ch = img.shape
img1 = img[0:h,0:w//2] #slice first H x W/2 part of image
img2 = cv2.cvtColor(img[0:h,w//2:w],cv2.COLOR_BGR2GRAY) #slice the other H x W/2 part of image
final = np.hstack((img1,cv2.cvtColor(img2,cv2.COLOR_GRAY2BGR))) #stack them up horizontally
cv2.imshow("Final Image",final)
cv2.waitKey(0)

