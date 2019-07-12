#!/usr/bin/env python
# coding:utf-8
"""
@author: zc12345 
@contact: 18292885866@163.com

@file: rgb2rgba.py
@time: 2019/7/12 21:20
@description:

"""
from PIL import Image
import numpy as np
import cv2


def cv2_add_alpha(img_path, save_path, bg_color=[255, 255, 255]):
    # image matting by bg color
    img = cv2.imread(img_path)
    b_channel, g_channel, r_channel = cv2.split(img)
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype)*255
    print(img.shape)
    w, h, c = img.shape
    for i in range(w):
        for j in range(h):
            if all(img[i][j] == bg_color):
                alpha_channel[i][j] = 0
    img_RGBA = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
    cv2.imwrite(save_path, img_RGBA)


def pil_add_alpha(img_path, save_path):
    # just add a mask
    img = Image.open(img_path)
    img = img.convert('RGBA')
    r, g, b, alpha = img.split()
    alpha = alpha.point(lambda i: i > 0 and 178)
    img.putalpha(alpha)
    img.save(save_path)


def pil_add_trans(img_path, save_path, factor=0.7):
    # just add a mask, img_blender can be a real img
    img = Image.open(img_path)
    img = img.convert('RGBA')
    img_blender = Image.new('RGBA', img.size, (0,0,0,0))
    img = Image.blend(img_blender, img, factor)
    img.save(save_path)


if __name__ == '__main__':
    img_path = 'test.png'
    save_path = 'output_rgba.png'
    cv2_add_alpha(img_path, save_path)