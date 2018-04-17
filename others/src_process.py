#!/usr/bin/python
#coding=utf-8
from __future__ import print_function
import numpy as np
import re
import jieba
from os import listdir, mkdir, walk
from os.path import exists, isfile, join, splitext, isdir

def run_coding(file_dir, out_dir):
    files = [f for f in listdir(input_path)] # 获取input_path文件夹下的所有文件
    index = 0
    if not exists(out_dir):# 如果输出文件夹不存在则创建文件夹
        mkdir(out_dir)
    for file_path in files:
        if splitext(file_path)[1] == '.srt': # 根据后缀名筛选其中的txt文件进行处理
            print('process', file_path)
            srt_path = join(file_dir, file_path)
            backup_path = join(out_dir, file_path)
            print(srt_path)
            print(backup_path)
            with open(srt_path, 'r') as f:
                with open(backup_path, 'w', encoding='utf8') as bf:
                    for line in f.readlines():
                        bf.write(line)
                        
def get_train(tgt_path, src_path, input_dir):
    files = [f for f in listdir(input_dir)] # 获取input_path文件夹下的所有文件
    with open(tgt_path, 'w', encoding='utf8') as tgt_f:
        with open(src_path, 'w', encoding='utf8') as src_f:
            for file in files:
                file_path = join(input_dir, file)
                if splitext(file)[1] == '.src':
                    with open(file_path, 'r', encoding='utf8') as f:
                        for line in f.readlines():
                            src_f.write(line)
                elif splitext(file)[1] == '.tgt':
                    with open(file_path, 'r', encoding='utf8') as f:
                        for line in f.readlines():
                            tgt_f.write(line)
    
def select_dev(tgt_path, src_path, dev_tgt_path, dev_src_path):
    with open(tgt_path,'r', encoding='utf8') as in_tgt:
        with open(dev_tgt_path,'w', encoding='utf8') as out_tgt:
            index = 0
            for line in in_tgt.readlines():
                if index % 10 == 0:
                    out_tgt.write(line)
                index += 1
    with open(src_path, 'r', encoding='utf8') as in_src:
        with open(dev_src_path,'w', encoding='utf8') as out_src:
            index = 0
            for line in in_src.readlines():
                if index % 10 == 0:
                    out_src.write(line)
                index += 1

def srtprocess(srt_path, tgt_path, src_path, out_path, index):
    tgt_path = join(out_path, str(index)+'.tgt')
    src_path = join(out_path, str(index)+'.src')
    with open(srt_path, 'r', encoding='utf8') as f:
        with open(tgt_path, 'w', encoding='utf8') as out_tgt:
            with open(src_path, 'w', encoding='utf8') as out_src:
                index = 0
                for line in f.readlines():
                    index +=1                        
                    if (index > 10) and (index % 5 == 4) :
                        cns_list = jieba.cut(line, cut_all = False)
                        cns = ' '.join(cns_list)
                        out_src.write('<s> '+cns[0:-1]+'</s>\n')
                    elif (index > 10) and (index % 5 == 3) :
                        out_tgt.write('<s> '+line[0:-1].lower()+' </s>\n')


def process(input_path, tgt_path, src_path, out_path):
    '''
    调用txt_process函数对待处理文件目录下所有txt文件进行处理
    '''
    files = [f for f in listdir(input_path)] # 获取input_path文件夹下的所有文件
    index = 0
    for file_path in files:
        index += 1
        if splitext(file_path)[1] == '.srt' : # 根据后缀名筛选其中的txt文件进行处理
            print('process', file_path)
            srt_path = join(input_path, file_path)
            srtprocess(srt_path, tgt_path, src_path, out_path, index) # 调用文件处理
            
if __name__ == "__main__":
    out_path = './out'      # 处理后会的文件所在路径
    input_path = './input'  # 待处理文件所在路径
    backup_dir = './backup'
    if not exists(out_path):# 如果输出文件夹不存在则创建文件夹
        mkdir(out_path)
    tgt_path = join(out_path, 'train.tgt')
    src_path = join(out_path, 'train.src')
    dev_tgt_path = join(out_path, 'dev.tgt')
    dev_src_path = join(out_path, 'dev.src')
    run_coding(input_path, backup_dir)
    process(backup_dir, tgt_path, src_path, out_path)
    get_train(tgt_path, src_path, out_path)
    select_dev(tgt_path, src_path, dev_tgt_path, dev_src_path)
    print('process over')
