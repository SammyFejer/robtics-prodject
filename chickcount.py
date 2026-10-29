from PIL import Image
#import pytesseract
import cv2
import os, sys, inspect #For dynamic filepaths
import numpy as np;
import heapq
from ultralytics import YOLO

model = YOLO("best (1).pt")
cap = cv2.VideoCapture('2camchickens.mp4')

while True:
    # im_src = cv2.imread('//home/uberputer/Documents/YOLO/left chickens.png', cv2.IMREAD_COLOR)
    # pts_src = np.array([[134, 110],[208, 107], [361, 231], [155, 237]])
    # ret, frame = cap.read()
    # if not ret:
    #       print("woopwoop ")
    #       break

   

    # im_dst = cv2.imread('//home/uberputer/Documents/YOLO/right 2.05.png', cv2.IMREAD_COLOR)
    # pts_dst = np.array([[123, 26],[190, 19], [322, 94], [147, 135]])
    # width = im_dst.shape[1] + im_src.shape[1]

    # h,status= cv2.findHomography(pts_src, pts_dst)
    # im_out = cv2.warpPerspective(im_src, h , (width,im_dst.shape[0]))
    # # im_out[0:im_dst.shape[0], 0:im_dst.shape[1]] = im_dst
    # cv2.circle(im_src, (pts_src[0]), 2 ,(255, 0, 100), -1)
    # cv2.circle(im_src, (pts_src[1]), 2 ,(0, 255, 255), -1)
    # cv2.circle(im_src, (pts_src[2]), 2 ,(255, 0, 0), -1)
    # cv2.circle(im_src, (pts_src[3]), 2 ,(0, 255, 0), -1)

    # cv2.circle(im_dst, (pts_dst[0]), 2 ,(255, 0, 100), -1)
    # cv2.circle(im_dst, (pts_dst[1]), 2 ,(0, 255, 255), -1)
    # cv2.circle(im_dst, (pts_dst[2]), 2 ,(255, 0, 0), -1)
    # cv2.circle(im_dst, (pts_dst[3]), 2 ,(0, 255, 0), -1)

    # results = model(source='left chickens.png', show=True, conf=0.05)
    results2 = model(source='chickens4.jpeg', show=True, conf=0.05)

   
    im_dst = results2[0].plot()
    

    # cv2.imshow('video',im_src )
    cv2.imshow('drawnall', im_dst)
    # cv2.imshow('out', im_out)
    print("loop complete")
    key = cv2.waitKey(0)
    if key == 27:
    
           break
cap.release()
cv2.destroyAllWindows()