# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 09:42:20 2019

@author: zc12345
@contact: 18292885866@163.com

@description:
"""
import os.path as osp
import json
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

def _load_json(json_path):
    data = json.load(open(json_path))
    return data['points']

class json2mat:
    def __init__(self, root_dir, lst_path, save_path, origin_img_shape=np.array([1280, 1024]), resized_img_shape=np.array([256, 256]), k=16):
        self._root_dir = root_dir
        self._lst_path = lst_path
        self._save_path = save_path
        self._origin_shape = origin_img_shape
        self._resized_shape = resized_img_shape
        self._k = k
        self._json_paths = []
        
    def _load_json_path(self):
        _path = osp.join(self._root_dir, self._lst_path)
        with open(_path, 'r') as f:
            for line in f.readlines():
                img, label, json_lbl, kpt_lbl = line.split()
                img_path = osp.join(self._root_dir, img).replace('\\', '/')
                kpt_path = osp.join(self._root_dir, kpt_lbl).replace('\\', '/')
                p = (img_path, kpt_path)
                assert osp.exists(img_path) and osp.exists(kpt_path), 'keypoint json file does not exist'
                self._json_paths.append(p)
        return self._json_paths
    
    def _check_pts(self, img, kpts):
        m, n = kpts.shape
        w, h = img.size
        assert m == self._k and n == 2
        assert np.max(kpts[:, 0]) < w and np.max(kpts[:, 1]) < h
        assert w == self._origin_shape[0] and h == self._origin_shape[1]
        
    def _check_new(self, img, kpts):
        m, n = kpts.shape
        w, h = img.size
        assert m == self._k and n == 2
        assert np.max(kpts[:, 0]) < w and np.max(kpts[:, 1]) < h
        assert w == self._resized_shape[0] and h == self._resized_shape[1]
    
    def _resize(self, img_path, kpt_path):
        img = Image.open(img_path)
        kpts = np.array(_load_json(kpt_path))
        self._check_pts(img, kpts)
        img = img.resize(self._resized_shape)
        _s = self._origin_shape / self._resized_shape
        kpts = kpts / _s
        kpts[kpts > self._resized_shape[0]-1] = self._resized_shape[0]-1
        kpts[kpts < 0 ] = 0
        plt.imshow(img)
        plt.plot(kpts[:,0], kpts[:,1])
        self._check_new(img, kpts)
        return img, kpts
        
    def convert(self):
        json_paths = self._load_json_path()
        num = len(json_paths)
        imgs = np.zeros((num, self._resized_shape[0], self._resized_shape[1], 3))
        kpts = np.zeros((num, self._k, 2))
        for i, (img_path, kpt_path) in enumerate(json_paths):
            img, kpt = self._resize(img_path, kpt_path)
            imgs[i] = img
            kpts[i] = kpt
        sio.savemat(self._save_path, {'imgPath': imgs, 'ptsAll': kpts})
         
def main():
    root_dir = '../../data/imgs'
    lst_path = 'train_full_lst.txt'
    save_path = 'data.mat'
    j2m = json2mat(root_dir, lst_path, save_path)
    j2m.convert()

if __name__ == '__main__':
    main()
