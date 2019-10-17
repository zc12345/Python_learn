# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:57:46 2019

@author: zc12345
@contact: 18292885866@163.com

@description:
"""
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

def im2bw(img, thres):
    img[img >= thres] = 0
    img[img < thres] = 255
    return img

def save_img(img, save_path, mode='RGB'):
    img = Image.fromarray(img.astype('uint8')).convert(mode)
    img.save(save_path)

def threshold_seg(img):
    '''
    params: img: input gray image
    params: threshold: init threshold
    return: binary image
    '''
    t = np.mean(img) #init threshold with mean value
    while True:
        seg = img >= t
        fg = img[seg]
        bg = img[~seg]
        t_next = 0.5 * (np.mean(fg) + np.mean(bg))
        if np.abs(t-t_next) < 0.5:
            return t_next
        t = t_next
        
def otsu_seg(img):
    ret1, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    return th1

def main():
    img_dir = 'DIP3E_Original_Images_CH10'
#    img_fn = 'Fig1038(a)(noisy_fingerprint).tif'
    img_fn = 'Fig1039(a)(polymersomes).tif'
    img_path = os.path.join(img_dir, img_fn)
    img = Image.open(img_path)
    img = np.array(img)
    threshold = otsu_seg(img)
#    threshold = threshold_seg(img)
    seg = im2bw(img, threshold)
    save_img(seg, 'test.png', mode='L')
    plt.imshow(seg)
    plt.show()
#    
if __name__ == '__main__':
    main()
