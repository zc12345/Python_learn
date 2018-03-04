#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__  import print_function
import numpy as np
import tkinter as tk
import time

def getMED(s1, s2, m, n):
    '''
    计算两个字符串s1和s2的最小编辑距离
    '''
    if m == 0:
        d = n
        return d
    if n == 0:
        d = m
        return d
    d1 = getMED(s1, s2, m-1, n) + 1
    d2 = getMED(s1, s2, m, n-1) + 1
    if s1[m - 1] == s2[n - 1]:
        d3 = getMED(s1, s2, m-1, n-1)
    else:
        d3 = getMED(s1, s2, m-1, n-1) + 2
    d = min(d1, d2, d3)
    return d

def getDistanceMatrix(s1, s2):
    '''
    根据getMED函数得到MED矩阵
    '''
    start = time.clock()
    d = np.zeros((len(s1) + 1, len(s2) + 1))

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            d[i][j] = getMED(s1, s2, i, j)
    end = time.clock()
    print(end - start)
    return d

def DMatrix(s1, s2):
    '''
    使用矩阵存储MED中间值，避免每一次值计算都要重新递归
    '''
    start = time.clock()
    d = np.zeros((len(s1) + 1, len(s2) + 1))

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0:
                d[i][j] = j
            elif j == 0:
                d[i][j] = i
            else:
                deletion = d[i-1][j] + 1
                insertion = d[i][j-1] + 1
                if s1[i-1] == s2[j-1]:
                    substitution = d[i-1][j-1]
                else:
                    substitution = d[i-1][j-1] + 2
                d[i,j] = min(deletion, insertion, substitution)
    end = time.clock()
    print(end - start)
    return d

def MainCLI():
    '''
    命令行模式
    '''
    s1 = input('Please input word 1:')
    s2 = input('Please input word 2:')
    distanceMatrix = DMatrix(s1, s2)
    d = distanceMatrix[len(s1)][len(s2)]
    print(distanceMatrix)
    print('Minimum Edit Distance is %d.' % (d))
    input('Press any key to exit.')
    return

def MainGUI():
    '''
    图形界面
    '''
    def getMEDBtn():
        nonlocal var_s1, var_s2, result
        s1 = var_s1.get()
        s2 = var_s2.get()
        distanceMatrix = DMatrix(s1, s2)
        d = distanceMatrix[len(s1)][len(s2)]
        result.insert('insert', int(d))

    def reset():
        nonlocal result
        print(result.get(1.0, tk.END))
        result.delete(1.0, tk.END)
    app = tk.Tk()
    app.title('计算最小编辑距离')
    app.geometry('300x300')
    tk.Label(app, text = 'word 1').place(x = 20, y = 20)
    tk.Label(app, text = 'word 2').place(x = 20, y = 60)
    tk.Label(app, text = '最小编辑距离').place(x = 20, y = 100)
    var_s1 = tk.StringVar()
    var_s2 = tk.StringVar()
    s1 = tk.Entry(app, textvariable = var_s1).place(x = 120, y = 20, width = 150, height = 20)
    s2 = tk.Entry(app, textvariable = var_s2).place(x = 120, y = 60, width = 150, height = 20)
    result = tk.Text(app)
    result.place(x = 120, y = 100, width = 150, height = 20)
    getBtn = tk.Button(app, text = '计算', command = getMEDBtn).place(x = 70, y = 140)
    resetBtn = tk.Button(app, text = '重置', command = reset).place(x = 200, y = 140)
    
    app.mainloop()
    return

if __name__ == "__main__":
    s1 = 'intention'
    s2 = 'execution'
    d = DMatrix(s1, s2)
    print(d)
    MainGUI()
