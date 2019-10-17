# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 22:13:43 2019

@author: zc12345
@contact: 18292885866@163.com

@description:
"""
import cv2
import numpy as np
from viz_flow import viz_flow

def dense_optical_flow(cap):
    ret, frame1 = cap.read()
    prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    while(1):
        ret, frame2 = cap.read()
        next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 6, 3, 5, 1.25, 0)
        bgr = viz_flow(flow)
        cv2.imshow("frame",frame2)
        cv2.imshow("flow",bgr)
        k = cv2.waitKey(30) & 0xff
        if k == ord('q') or k == 27:# 'ESC' or 'q' to quit
            break
        elif k == ord('s'):
            cv2.imwrite('opticalfb.png',frame2)
            cv2.imwrite('opticalhsv.png',bgr)
        prvs = next

def lk_optical_flow(cap):
    # params for ShiTomasi corner detection
    feature_params = dict( maxCorners = 100,
                    qualityLevel = 0.3,
                    minDistance = 7,
                    blockSize = 7 )
    
    # Parameters for lucas kanade optical flow
    lk_params = dict( winSize = (15,15),
                    maxLevel = 2,
                    criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
    
    # Create some random colors
    color = np.random.randint(0,255,(100,3))
    
    # Take first frame and find corners in it
    ret, old_frame = cap.read()
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
    
    # Create a mask image for drawing purposes
    mask = np.zeros_like(old_frame)
    
    while(1):
        ret,frame = cap.read()
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        # calculate optical flow
        p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    
        # Select good points
        good_new = p1[st==1]
        good_old = p0[st==1]
    
        # draw the tracks
        for i,(new,old) in enumerate(zip(good_new,good_old)):
            a,b = new.ravel()
            c,d = old.ravel()
            mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
            frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
    
        img = cv2.add(frame,mask)
    
        cv2.imshow('frame',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    
        # Now update the previous frame and previous points
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1,1,2)

if __name__ == "__main__":
    cap = cv2.VideoCapture("2006.mp4")
#    dense_optical_flow(cap)
    lk_optical_flow(cap)
    
    cap.release()
    cv2.destroyAllWindows()