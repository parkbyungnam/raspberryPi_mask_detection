import cv2
import numpy as np
import os

def Rotate(src, degrees):
    if degrees == 90:
        dst = cv2.transpose(src)
        dst = cv2.flip(dst, 1)

    elif degrees == 180:
        dst = cv2.flip(src, -1)

    elif degrees == 270:
        dst = cv2.transpose(src)
        dst = cv2.flip(dst, 0)
    else:
        dst = null
    return dst

cam = cv2.VideoCapture(-1)
cam.set(3,480)
cam.set(4,640)
while True:
    ret, img = cam.read()
    
    img= Rotate(img,270)
    cv2.imshow('img',img)
    if cv2.waitKey(30)==ord('q'):
        break
cam.release()
cam.destroyAllWindows()