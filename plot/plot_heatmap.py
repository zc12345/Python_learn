import os
import json
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import logging
import math
from labelme import utils

#0为背景
classname_to_id = {"road": 1, "car":2}
target_cls = ['car']


def gaussian_radius(det_size, min_overlap=0.7):
    # https://github.com/zju3dv/snake/blob/master/lib/utils/data_utils.py
    height, width = det_size

    a1 = 1
    b1 = (height + width)
    c1 = width * height * (1 - min_overlap) / (1 + min_overlap)
    sq1 = np.sqrt(b1 ** 2 - 4 * a1 * c1)
    r1 = (b1 + sq1) / 2

    a2 = 4
    b2 = 2 * (height + width)
    c2 = (1 - min_overlap) * width * height
    sq2 = np.sqrt(b2 ** 2 - 4 * a2 * c2)
    r2 = (b2 + sq2) / 2

    a3 = 4 * min_overlap
    b3 = -2 * min_overlap * (height + width)
    c3 = (min_overlap - 1) * width * height
    if b3 ** 2 - 4 * a3 * c3 < 0:
        r3 = min(r1, r2)
    else:
        sq3 = np.sqrt(b3 ** 2 - 4 * a3 * c3)
        r3 = (b3 + sq3) / 2
    return min(r1, r2, r3)

def gaussian2D(shape, sigma=(1, 1), rho=0): 
    # https://github.com/zju3dv/snake/blob/master/lib/utils/data_utils.py
    if not isinstance(sigma, tuple):
        sigma = (sigma, sigma)
    sigma_x, sigma_y = sigma

    m, n = [(ss - 1.) / 2. for ss in shape]
    y, x = np.ogrid[-m:m+1, -n:n+1]

    energy = (x * x) / (sigma_x * sigma_x) - 2 * rho * x * y / \
        (sigma_x * sigma_y) + (y * y) / (sigma_y * sigma_y)
    h = np.exp(-energy / (2 * (1 - rho * rho)))
    h[h < np.finfo(h.dtype).eps * h.max()] = 0
    return h

def draw_umich_gaussian(heatmap, center, radius, k=1):
    # https://github.com/zju3dv/snake/blob/master/lib/utils/data_utils.py
    diameter = 2 * radius + 1
    gaussian = gaussian2D((diameter, diameter), sigma=diameter / 6)

    x, y = int(center[0]), int(center[1])

    height, width = heatmap.shape[0:2]

    left, right = min(x, radius), min(width - x, radius + 1)
    top, bottom = min(y, radius), min(height - y, radius + 1)

    masked_heatmap = heatmap[y - top:y + bottom, x - left:x + right]
    masked_gaussian = gaussian[radius - top:radius +
                               bottom, radius - left:radius + right]
    if min(masked_gaussian.shape) > 0 and min(masked_heatmap.shape) > 0:  # TODO debug
        np.maximum(masked_heatmap, masked_gaussian * k, out=masked_heatmap)
    return heatmap

def draw_umich_gaussian2(heatmap, center, radius, k=1, ratio=1):
    diameter = 2 * radius + 1
    sigma_ = diameter / 6
    sigma = (sigma_, sigma_*ratio)
    # gaussian = gaussian2D((diameter, diameter), sigma=diameter / 6)
    gaussian = gaussian2D((diameter, diameter), sigma=sigma)

    x, y = int(center[0]), int(center[1])

    height, width = heatmap.shape[0:2]

    left, right = min(x, radius), min(width - x, radius + 1)
    top, bottom = min(y, radius), min(height - y, radius + 1)

    masked_heatmap = heatmap[y - top:y + bottom, x - left:x + right]
    masked_gaussian = gaussian[radius - top:radius +
                               bottom, radius - left:radius + right]
    if min(masked_gaussian.shape) > 0 and min(masked_heatmap.shape) > 0:  # TODO debug
        np.maximum(masked_heatmap, masked_gaussian * k, out=masked_heatmap)
    return heatmap

class PlotHeatmap:
    def __init__(self, img):
        self.img = img
    
    def plot_hm(self, bbox, type='xx'):
        ct_hm = np.zeros(self.img.size[::-1])
        x1, y1, w, h = bbox
        center = (x1+w/2, y1+h/2)
        radius = gaussian_radius((math.ceil(h), math.ceil(w)))*4
        radius = max(0, int(radius))
        if type == 'xx':
            hm = draw_umich_gaussian(ct_hm, center, radius)
        elif type == 'xy':
            hm = draw_umich_gaussian2(ct_hm, center, radius, ratio=h/w)
        return hm
        

class Polygon2Bbox:
    def __init__(self):
        self.annotations = []

    # 由json文件构建bbox标注
    def to_bbox(self, json_path):
        obj = self.read_jsonfile(json_path)
        shapes = obj['shapes']
        for shape in shapes:
            if shape['label'] not in target_cls:
                continue
            annotation = {}
            points = shape['points']
            bbox = self._get_box(points)
            annotation['label'] = shape['label']
            annotation['points'] = points
            annotation['bbox'] = bbox
            return bbox
        logging.info('No target cls objs!!!')
        return None

    # 读取json文件，返回一个json对象
    def read_jsonfile(self, path):
        with open(path, "r", encoding='utf-8') as f:
            return json.load(f)

    # COCO的格式： [x1,y1,w,h] 对应COCO的bbox格式
    def _get_box(self, points):
        min_x = min_y = np.inf
        max_x = max_y = 0
        for x, y in points:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        return [min_x, min_y, max_x - min_x, max_y - min_y]


if __name__ == '__main__':
    json_path = 'D:/documents/data/xjtu_plus/label/Section27CameraC_00909c.json'
    img_path = 'D:/documents/data/xjtu_plus/img/Section27CameraC_00909c.jpg'
    img = Image.open(img_path)
    obj = Polygon2Bbox()
    bbox = obj.to_bbox(json_path)
    plot = PlotHeatmap(img)
    hm_type = 'xx'
    hm = plot.plot_hm(bbox, type=hm_type)

    fig, ax = plt.subplots()
    plt.axis('off')
    plt.subplots_adjust(top=1, bottom=0, left=0,
                        right=1, hspace=0, wspace=0)
    # plt.margins(0, 0)
    
    plt.imshow(img)
    plt.imshow(hm, alpha=.7)
    plt.gca().add_patch(plt.Rectangle(xy=(bbox[0], bbox[1]),
                                      width=bbox[2],
                                      height=bbox[3],
                                      edgecolor='red', linestyle='--',
                                      fill=False, linewidth=.6))
    # plt.savefig('hm_{}.pdf'.format(hm_type), dpi=150, format='pdf')
    plt.show()

