# -*- coding: utf-8 -*-
"""
@author: zc12345 
@contact: 18292885866@163.com

@file: isClockwise.py
@time: 2019/7/30 10:02
@description:
"""

import os
import os.path as osp
import json
import numpy as np
import logging
import datetime
import matplotlib.pyplot as plt
from PIL import Image

now = datetime.datetime.now().strftime('%Y-%m-%d-%H')

logging.basicConfig(level=logging.DEBUG,
                    filename='debug-{}.log'.format(now),
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='a')

class normPointLabel:
    def __init__(self, left_top=np.array([0, 0]), right_bottom=np.array([1279, 1023]), delta=5, k=8):
        self.coord1 = left_top # left top coordinate in image
        self.coord2 = right_bottom # right bottom coordinate in image
        self.delta = delta # labels near image boundary (< delta pixel) are considered as boundary points
        self.k = k # point number for one side
        
    def _load(self, json_path):
        # load json file
        data = json.load(open(json_path))
        for shape in data['shapes']:
            if shape['label'] == 'road':
                return np.array(shape['points'])
        logging.error('No road annotation.')
        return None
    
    def _refineLabel(self, pts):
        # refine annotation points close to corner
        for i, pt in enumerate(pts):
            res1 = np.abs(pt - self.coord1)
            res2 = np.abs(pt - self.coord2)
            for j, p in enumerate(pt):
                if res1[j] < self.delta:
                    pts[i, j] = self.coord1[j]
                elif res2[j] < self.delta:
                    pts[i, j] = self.coord2[j]
        return pts
    
    def _isClockwise(self, pts):
        pass
    
    def _isClockwiseBottom(self, pts):
        # check whether it is clockwise from bottom points
        stat = None
        for index, point in enumerate(pts):
            if point[1] == self.coord2[1]:
                next_point = pts[0] if index == len(pts) - 1 else pts[index + 1]
                if next_point[1] == self.coord2[1] and np.sum(next_point - point) > 0:
                    stat = False
                    logging.info('Judge from bottom line: {}'.format(stat))
                elif next_point[1] == self.coord2[1] and np.sum(next_point - point) < 0:
                    stat = True
                    logging.info('Judge from bottom line: {}'.format(stat))
        assert stat is not None, 'Clockwise check error'
        return stat
    
    def _resortPts(self, pts):
        # resort point order from left bottom
        start = 0
        left_min = self.coord2[0]
        for index, point in enumerate(pts):
            if point[1] == self.coord2[1] and point[0] < left_min:
                left_min = point[0]
                start = index
        sorted_pts = np.zeros(pts.shape)
        sorted_pts[:pts.shape[0]-start] = pts[start:]
        sorted_pts[pts.shape[0]-start:] = pts[:start]
        return sorted_pts
    
    def _getCorner(self, pts):
        '''
        Type1: left_bottom -- left_mid -- left_top -- right_top -- right_mid -- right_bottom
        Type2: left_bottom -- left_top -- right_top -- right_bottom
        Type3: left_bottom -- left_mid -- left_top -- right_top -- right_bottom
        Type4: left_bottom -- left_top -- right_top -- right_mid -- right_bottom
        '''
        left_bottom_index = left_mid_index = left_top_index = right_top_index = right_mid_index = right_bottom_index = None
        m, n = pts.shape
        left_bottom_index, right_bottom_index = 0, -1
        # get bottom points and mid points
        if (not pts[0, 0] == self.coord1[0]) and (not pts[-1, 0] == self.coord2[0]):
            logging.info('Mid points are None.')
            left_mid_index, right_mid_index = 0, -1
        elif (not pts[0, 0] == self.coord1[0]) and pts[-1, 0] == self.coord2[0]:
            rights = np.ones(pts.shape) * max(self.coord2) # init with inf_max number
            for i, pt in enumerate(pts):
                if pt[0] == self.coord2[0]:
                    rights[i] = pt
            left_mid_index, right_mid_index = 0, rights[:, 1].argmin()
        elif pts[0, 0] == self.coord1[0] and (not pts[-1, 0] == self.coord2[0]):
            lefts = np.ones(pts.shape) * max(self.coord2) # init with inf_max number
            for i, pt in enumerate(pts):
                if pt[0] == self.coord1[0]:
                    lefts[i] = pt
            left_mid_index, right_mid_index = lefts[:, 1].argmin(), -1
        elif pts[0, 0] == self.coord1[0] and pts[-1, 0] == self.coord2[0]:
            lefts = np.ones(pts.shape) * max(self.coord2)
            rights = np.ones(pts.shape) * max(self.coord2) # init with inf_max number
            for i, pt in enumerate(pts):
                if pt[0] == self.coord2[0]:
                    rights[i] = pt
                if pt[0] == self.coord1[0]:
                    lefts[i] = pt
            right_mid_index, left_mid_index = rights[:, 1].argmin(), lefts[:, 1].argmin()
        else:
            logging.error('bottom point index is abnormal.')
        # get top points
        top_index = pts[:,1].argmin()
        if top_index > 1 and top_index < m-2:
            candiate0 = pts[top_index]
            candiate1 = pts[top_index - 1]
            candiate2 = pts[top_index + 1]
            dist1 = np.sum((candiate1 - candiate0)**2)
            dist2 = np.sum((candiate2 - candiate0)**2)
            if dist1 < dist2:
                # left_top, right_top = candiate1, candiate0
                left_top_index, right_top_index = top_index - 1, top_index
            else:
                # left_top, right_top = candiate0, candiate2
                left_top_index, right_top_index = top_index, top_index + 1
        else:
            logging.error("top point index is abnormal.")
        corner_pts_index = [left_bottom_index, left_mid_index, left_top_index, right_top_index, right_mid_index, right_bottom_index]
        
        # check corner points
        assert not (None in corner_pts_index), logging.error('point index is None.')
        return corner_pts_index
    
    def _interpDiv(self, pts, corner_pts_index):
        assert len(corner_pts_index) == 6, 'corner points index is abnormal'
        k1 = k2 = self.k
        if not corner_pts_index[0] == corner_pts_index[1]:
            k1 = k1 - 1
        if not corner_pts_index[-2] == corner_pts_index[-1]:
            k2 = k2 - 1
        left_i1, left_i2, right_i1, right_i2 = corner_pts_index[1], corner_pts_index[2], corner_pts_index[3], corner_pts_index[4]
        left_pts, right_pts = pts[left_i1: left_i2+1], pts[right_i1: right_i2+1]
        _x1 = np.linspace(pts[left_i1][0], pts[left_i2][0], k1)
        _x2 = np.linspace(pts[right_i1][0], pts[right_i2][0], k2)
        _y1 = np.interp(_x1, left_pts[:, 0], left_pts[:, 1])
        _y2 = np.interp(_x2, right_pts[:, 0], right_pts[:, 1])
        _x1, _x2, _y1, _y2 = np.trunc(_x1), np.trunc(_x2), np.trunc(_y1), np.trunc(_y2)
        _x = np.concatenate((_x1, _x2), axis=0)
        _y = np.concatenate((_y1, _y2), axis=0)
        _pts = np.array([_x, _y]).T
        if not corner_pts_index[0] == corner_pts_index[1]:
            left_pt = pts[corner_pts_index[0]].reshape((1,2))
            _pts = np.concatenate((left_pt, _pts), axis=0)
        if not corner_pts_index[-2] == corner_pts_index[-1]:
            right_pt = pts[corner_pts_index[-1]].reshape((1,2))
            _pts = np.concatenate((_pts, right_pt), axis=0)
            
        return _pts
        
    def normLabel(self, json_path):
        # from LabelMe road annotation to fixed number points annotation
        pts = self._load(json_path)
        pts = np.trunc(pts)
        assert pts is not None, 'No point label'
        pts = self._refineLabel(pts)
        flag = self._isClockwiseBottom(pts)
        if not flag:
            pts = np.flip(pts, axis=0)
        pts = self._resortPts(pts)
        corner_pts_index = self._getCorner(pts)
        final_pts = self._interpDiv(pts, corner_pts_index)
        return pts, final_pts
    
    def batchNorm(self, json_dir, save_dir, save_fig_dir, img_dir):
        for root, dirs, files in os.walk(json_dir):
            logging.info('Dir: {}'.format(root))
            for file in files:
                if file.split('.')[-1] == 'json':
                    logging.info('BEGIN load file: {}'.format(file))
                    img_path = osp.join(img_dir, file.split('.')[0] + '.jpg')
                    json_path = osp.join(root, file)
                    save_path = osp.join(save_dir, file)
                    save_fig_path = osp.join(save_fig_dir, file.split('.')[0] + '_fig.png')
                    pts, norm_pts = self.normLabel(json_path)
                    
                    # --- plot points to check result ---
                    plt.figure(0)
                    img = Image.open(img_path)
                    w, h = img.size
                    plt.imshow(img)
                    plt.plot(pts[:,0], pts[:, 1], '-*')
                    for i, (x, y) in enumerate(zip(norm_pts[:,0],norm_pts[:,1])):
                        plt.text(x, y+1, str(i), ha = 'center',va = 'bottom',fontsize=20)
                    plt.plot(norm_pts[:,0],norm_pts[:,1],
                             markersize=10, marker='o', color='red', markerfacecolor='blue',
                             linestyle='dashed', linewidth=3, markeredgecolor='m')
                    fig = plt.gcf()
                    fig.set_size_inches(w / 100.0, h / 100.0)  # 输出width*height像素
                    plt.gca().xaxis.set_major_locator(plt.NullLocator())
                    plt.gca().yaxis.set_major_locator(plt.NullLocator())
                    plt.subplots_adjust(top=1, bottom=0, left=0, right=1, hspace=0, wspace=0)
                    plt.margins(0, 0)
                    plt.savefig(save_path, format='png', transparent=True)
                    plt.savefig(save_fig_path)
                    plt.close(0)
                    plt.show()
                    # --- plot end ---
                    
                    res = {
                            "label": "road",
                            "points": norm_pts.tolist()
                            }
                    with open(save_path, 'w', encoding='utf-8') as f:
                        json.dump(res, f, sort_keys=True, indent=4)
                    logging.info('END save.')

def main():
    root_path = '../../data/imgs'
    set_dir = 'sequence-3'
    npl = normPointLabel()
    img_dir = osp.join(root_path, set_dir, 'img')
    json_dir = osp.join(root_path, set_dir, 'label')
    save_dir = osp.join(root_path, set_dir, 'keypoint_label')
    save_fig_dir = osp.join(root_path, set_dir, 'keypoint_label_fig')
    if not osp.exists(save_dir):
        os.mkdir(save_dir)
    if not osp.exists(save_fig_dir):
        os.mkdir(save_fig_dir)
    npl.batchNorm(json_dir, save_dir, save_fig_dir, img_dir)


if __name__ == '__main__':
    main()
