#!/usr/bin/python
#coding=utf-8
from __future__ import print_function
import numpy as np
import re
from os import listdir, mkdir
from os.path import exists, isfile, join, splitext, isdir

def txt_process(file_path, input_path, out_path):
    '''
    处理单个文件
    '''
    input_file_path = join(input_path, file_path)
    out_file_path = join(out_path, file_path)
    with open(input_file_path,'r') as f: # 打开待处理文件
        with open(out_file_path, 'w') as outf: # 打开待写入的文件
            for line in f.readlines(): # 逐行读取文件内容
                s = line.split(' ') # 根据空格进行分割每行
                #print(s)
                if len(s) >6 and s[0] == 'sel' and s[3] == 'begin': # 根据行内容进行判断是否需要修改
                    if not (s[6] == ''): # 部分分割会出现s[6]为空字符串的情形，此处s[7]为要覆盖写的内容
                        #print(s[6])
                        n = float(s[6])
                        s[6] = ('%.2f' % (n + np.random.randn() - 0.5)) # np.random.rand()生成(0,1)区间内的随机数
                    else:
                        n = float(s[7])
                        s[7] = ('%.2f' % (n + np.random.randn() - 0.5))
                outs = " ".join(str(i) for i in s) # 再将处理后的字符串数组拼接回去
                outf.write(''.join(outs)) # 写入输出文件

def process(input_path, out_path):
    '''
    调用txt_process函数对待处理文件目录下所有txt文件进行处理
    '''
    if not exists(out_path):# 如果输出文件夹不存在则创建文件夹
        mkdir(out_path)
    files = [f for f in listdir(input_path)] # 获取input_path文件夹下的所有文件
    for file_path in files:
        if splitext(file_path)[1] == '.txt': # 根据后缀名筛选其中的txt文件进行处理
            print('process', file_path)
            txt_process(file_path, input_path, out_path) # 调用文件处理

if __name__ == "__main__":
    out_path = './out'      # 处理后会的文件所在路径
    input_path = './input'  # 待处理文件所在路径
    process(input_path, out_path)
    print('process over')
