import os
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def pts2seg(pts, tgt_path):
    img_shape = [1024, 1280]
    mask = np.zeros(img_shape,dtype = 'uint8')
    cv2.drawContours(mask,[pts],0,255,-1)
    im = Image.fromarray(mask)
    # plt.imshow(im)
    # plt.show()
    im.save(tgt_path)

def read_file(file_path, k):
    '''
    anno_file: xxx.txt
    content like:
    21 512
    103 471
    ...
    1177 388
    1259 409
    '''
    kpts = np.zeros((k + 2, 2), dtype='int32')
    kpts[0] = [0,1024]
    i = 1
    with open(file_path, 'r') as f:
        for line in f.readlines():
            x, y = line.split()
            kpts[i] = [x, y]
            i += 1
    kpts[i] = [1280, 1024]
    return kpts

def batch_process(anno_dir, mask_dir, k):
    for root, dirs, files in os.walk(anno_dir):
        for f in files:
            if f[-3:] == 'txt':
                anno_path = os.path.join(root, f)
                tgt_path = os.path.join(mask_dir, f[:-4]+'.png')
                kpts = read_file(anno_path, k)
                pts2seg(kpts, tgt_path)
                print(tgt_path)

def main():
    anno_dir = '../../keypoint_detection/data/val/prediction-v5-16pts'
    mask_dir = './mask'
    k = 16
    batch_process(anno_dir, mask_dir, k)

if __name__ == '__main__':
    main()
    

