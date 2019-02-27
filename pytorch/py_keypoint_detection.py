#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 15:19:21 2018

@author: zc12345
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import torch
from torch import nn, optim
from torch.nn import functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import math

def get_heatmap(joints_list, target_size):
    dataset_size = joints_list.shape[0]
    maps = joints_list.shape[1]
    height = 248
    width = 248
    sigma = 1.0
    heatmaps = np.zeros((dataset_size, maps, target_size[0], target_size[1]), dtype=np.float32)
    for idj, joints in enumerate(joints_list):
        heatmap = np.zeros((maps, height, width), dtype=np.float32)
        ##全部heatmap都初始化为0
        for idx, point in enumerate(joints):
            if point[0] < 0 or point[1] < 0: 
                continue
            put_heatmap(heatmap, idx, point, sigma)
        heatmap = heatmap.transpose((2, 1, 0)) ##self.height, self.width, CocoMetadata.__coco_parts
        # background
        # heatmap[:, :, -1] = np.clip(1 - np.amax(heatmap, axis=2), 0.0, 1.0)  
        if target_size:
            heatmap = cv2.resize(heatmap, target_size, interpolation=cv2.INTER_AREA) #插值resize
        heatmap = heatmap.transpose((2, 1, 0))
        heatmaps[idj, :, :, :] = heatmap
    
    return heatmaps

def put_heatmap(heatmap, plane_idx, center, sigma):
    center_x, center_y = center
    _, height, width = heatmap.shape[:3]
    th = 4.6052
    delta = math.sqrt(th * 2)

    x0 = int(max(0, center_x - delta * sigma))
    y0 = int(max(0, center_y - delta * sigma))

    x1 = int(min(width, center_x + delta * sigma))
    y1 = int(min(height, center_y + delta * sigma))

    for y in range(y0, y1):
        for x in range(x0, x1):
            d = (x - center_x) ** 2 + (y - center_y) ** 2  
            exp = d / 2.0 / sigma / sigma  
            if exp > th:
                continue
            heatmap[plane_idx][y][x] = max(heatmap[plane_idx][y][x], math.exp(-exp))
            heatmap[plane_idx][y][x] = min(heatmap[plane_idx][y][x], 1.0)
            
class keypointNet(nn.Module):
    def __init__(self):
        super(keypointNet, self).__init__()
        self.outNode = 16
        self.outPairNode = 15
        self.feature1 = nn.Sequential(
                nn.Conv2d(3, 64, kernel_size=3, padding=1),
                nn.ReLU(True),
                nn.Conv2d(64, 64, kernel_size=3, padding=1),
                nn.ReLU(True),
                nn.Dropout(),
                nn.MaxPool2d(kernel_size=2, stride=2),
                
                nn.Conv2d(64, 64, kernel_size=3, padding=1),
                nn.ReLU(True),
                nn.Conv2d(64, 128, kernel_size=3, padding=1),
                nn.ReLU(True),
                nn.Dropout(),
                nn.MaxPool2d(kernel_size=2, stride=2),
                
                nn.Conv2d(128, 128, kernel_size=3, padding=1),
                nn.ReLU(True),
                nn.Conv2d(128, 128, kernel_size=3, padding=1),
                nn.ReLU(True),
                nn.Dropout(),
                )
        self.feature2 = nn.Sequential(
                nn.Conv2d(128, 256, kernel_size=9, padding=4),
                nn.ReLU(True),
                nn.Conv2d(256, 512, kernel_size=9, padding=4),
                nn.ReLU(True),
                nn.Dropout(),
                
                nn.Conv2d(512, 256, kernel_size=1),
                nn.ReLU(True),
                nn.Conv2d(256, 256, kernel_size=1),
                nn.ReLU(True),
                nn.Dropout(),                
                )
        self.feature3 = nn.Sequential(
                nn.Conv2d(384, 64, kernel_size=7, padding=3),
                nn.ReLU(True),
                nn.Conv2d(64, 64, kernel_size=13, padding=6),
                nn.ReLU(True),
                nn.Dropout(),
                
                nn.Conv2d(64, 128, kernel_size=13, padding=6),
                nn.ReLU(True),
                nn.Conv2d(128, 256, kernel_size=1),
                nn.ReLU(True),
                nn.Dropout(),
                )
        self.heatmap = nn.Sequential(
                nn.Conv2d(256, self.outNode + self.outPairNode, kernel_size = 1)
                )
        #self._initialize_weights()
            
    def forward(self, x):
        x1 = self.feature1(x)
        x2 = self.feature2(x1)
        heatmap1 = self.heatmap(x2)
        x3 = [x1.permute(1,0,2,3), x2.permute(1,0,2,3)]
        x3 = torch.cat(x3)
        x4 = self.feature3(x3.permute(1,0,2,3))
        x5 = [x1.permute(1,0,2,3), x4.permute(1,0,2,3)]
        x5 = torch.cat(x5)
        x6 = self.feature3(x5.permute(1,0,2,3))
        x7 = [x1.permute(1,0,2,3), x6.permute(1,0,2,3)]
        x7 = torch.cat(x7)
        x8 = self.feature3(x7.permute(1,0,2,3))
        heatmap2 = self.heatmap(x4)
        heatmap3 = self.heatmap(x6)
        heatmap4 = self.heatmap(x8)
        return heatmap4

def load_data():
    pass
    
def train():
    net = keypointNet()
    target_size = (62, 62)
    dataset_size = 2
    mpii_pts = 16
    mpii_parts = list(zip(
        [1, 2, 3, 4, 5, 6, 7,  8,  9,  11, 12, 13, 14, 14, 15, 7],
        [2, 3, 7, 5, 6, 4, 10, 10, 10, 12, 13, 8,  8,  15, 16, 8]
        ))

    for epoch in range(10):
        inputs = torch.randn(dataset_size ,3,248,248)
        labels = torch.randn(dataset_size ,mpii_pts,2)
        target = get_heatmap(labels.numpy(), target_size)
        #target2 = get_vectormap(labels.numpy(), mpii_parts, target_size)
        target = torch.from_numpy(target)
        
        optimizer = optim.SGD(net.parameters(), lr = 0.001)
        optimizer.zero_grad()

        #net.zero_grad()
        output = net(inputs)
        criterion = nn.MSELoss()
        loss = criterion(output, target)
        print("epoch %s loss = %.5f"%(epoch, loss))
        loss.backward()
        optimizer.step()

def test():
    pass
    
if __name__ == "__main__":
    train()
