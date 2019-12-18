# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:57:42 2019

@author: zc12345
@contact: 18292885866@163.com

@description:
"""
import cv2
import numpy as np
import os.path
import glob
from viz_flow import viz_flow

def video2imgs(video_name, frames_dir):
    cap = cv2.VideoCapture(video_name)
    i = 0
    while cv2.waitKey(1) < 0:
        hasFrame,frame=cap.read()
        if not hasFrame:
            break
        cv2.imwrite(frames_dir + '/core-{:03d}.jpg'.format(i),frame)
        i = i + 1

def imgs2video(imgs_dir, save_name, src_file):
    cap = cv2.VideoCapture(src_file)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    fps = cap.get(cv2.CAP_PROP_FPS)
    video_writer = cv2.VideoWriter(
            save_name, cv2.VideoWriter_fourcc('M','J','P','G'), fps, 
            (round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
    # no glob, need number-index increasing
    imgs = glob.glob(os.path.join(imgs_dir, '*.jpg'))
    for i in range(len(imgs)):
        imgname = os.path.join(imgs_dir, 'optic-{:03d}.jpg'.format(i))
        frame = cv2.imread(imgname)
        video_writer.write(frame.astype(np.uint8))
    video_writer.release()

def dense_optical_flow(frame1, frame2, save_path):
    prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 6, 3, 5, 1.25, 0)
    bgr = viz_flow(flow)
    cv2.imwrite(save_path,bgr)


def dense_optic_flow(in_video, out_video):
    cap = cv2.VideoCapture(in_video)
    ret, frame1 = cap.read()
    prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    ret, frame2 = cap.read()
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    writer = cv2.VideoWriter(out_video,
                  cv2.VideoWriter_fourcc('I', '4', '2', '0'),
                  30, # fps
                  (width, height//2)) # resolution
    while ret:
        next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 6, 3, 5, 1.25, 0)
        bgr = viz_flow(flow)
        bgr = cv2.resize(bgr, (width//2, height//2))
        frame2 = cv2.resize(frame2, (width//2, height//2))

        img = np.hstack((frame2, bgr))
#        cv2.imshow('merge', img)
#        cv2.waitKey(1)
        writer.write(img)
        prvs = next
        ret, frame2 = cap.read()
        
    writer.release()
    cap.release()
    cv2.destroyAllWindows()

def main():
    video_name = 'ym.mkv'
    optic_video = 'ym_optic.mp4'
    dense_optic_flow(video_name, optic_video)
#    frames_dir = 'demo'
#    optic_dir = 'optic_demo'
#    video2imgs(video_name, frames_dir)
#    imgs = glob.glob(os.path.join(frames_dir, '*.jpg'))
#    for i in range(len(imgs) - 1):
#        frame1 = cv2.imread(os.path.join(frames_dir, 'core-{:03d}.jpg'.format(i)))
#        frame2 = cv2.imread(os.path.join(frames_dir, 'core-{:03d}.jpg'.format(i+1)))
#        save_path = os.path.join(optic_dir, 'optic-{:03d}.jpg'.format(i))
#        dense_optical_flow(frame1, frame2, save_path)
#    imgs2video(optic_dir, optic_video, video_name)

if __name__ == '__main__':
    main()
