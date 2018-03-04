#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__  import print_function
import math
import random

def function(x):
    '''
    定义目标函数
    '''
    r = math.sqrt((x[0]-50)**2 + (x[1]-50)**2) + math.e
    f = math.sin(r)/r + 1
    return -f

def global_optimization(N, step, epsilon, var_num, x, nu = 1):
    '''
    随机游走算法求出目标函数的全局最优解
    产生n个向量u，求其中的最小
    N: 迭代次数
    step: 初始步长，步长越大寻解空间越大，越不容易陷入局部最优值，但是相应的也需要迭代更多次数
    epsilon: 终止循环的精度阈值
    var_num: 变量数目 = len(x)
    x: 初始点坐标
    nu: 每次随机生成向量u的数目，默认为1。值增大会降低对于初始点的依赖
    '''
    print("迭代次数:",N)
    print("初始步长:",step)
    print("epsilon:",epsilon)
    print("变量数目:",var_num)
    print("初始点坐标:",x)
    walk_num = 1
    # 开始随机游走
    while(step > epsilon):
        k = 1 # 初始化计数器
        while(k < N):
            x1_list = [] # 存放x1的列表
            for i in range(nu):
                u = [random.uniform(-1,1) for i in range(var_num)] # 随机向量
                u1 = [u[i]/math.sqrt(sum([u[i]**2 for i in range(var_num)])) for i in range(var_num)] # u1 为标准化之后的随机向量
                x1 = [x[i] + step*u1[i] for i in range(var_num)]
                x1_list.append(x1)
            f1_list = [function(x) for x in x1_list]
            f1_min = min(f1_list)
            x11 = x1_list[f1_list.index(f1_min)] # 最小的f对应的x值
            if(f1_min < function(x)): # 如果找到了更优点
                k = 1
                x = x11
            else:
                k += 1
        step = step/2
        print("第%d次随机游走完成。" % walk_num)
        print(x)
        walk_num += 1
    print("随机游走次数:",walk_num-1)
    print("最终最优点:",x)
    print("最终最优值:",function(x))

def personalRank(G, alpha, root, n):
    '''
    使用随机游走算法PersonalRank实现基于图的推荐
    G: 图
    alpha: 决定继续访问的概率
    root: 出发节点
    n: 迭代次数
    return: 概率矩阵。初始时出发节点被访问概率为1，其余为0；迭代结束后各个节点的权重即为被访问的概率，和为1
    '''
    rank = dict()  
    rank = {x:0 for x in G.keys()}  
    rank[root] = 1  
    #开始迭代  
    for k in range(n):  
        tmp = {x:0 for x in G.keys()}  
        #取节点i和它的出边尾节点集合ri  
        for i, ri in G.items():  
            #取节点i的出边的尾节点j以及边E(i,j)的权重wij, 边的权重都为1，在这不起实际作用  
            for j, wij in ri.items():  
                #i是j的其中一条入边的首节点，因此需要遍历图找到j的入边的首节点，  
                #这个遍历过程就是此处的2层for循环，一次遍历就是一次游走  
                tmp[j] += alpha * rank[i] / (1.0 * len(ri))
        #每次游走都是从root节点出发，因此root节点的权重需要加上(1 - alpha)    
        tmp[root] += (1 - alpha)  
        rank = tmp
        
    #recommand = sorted(rank.items(),key=lambda x:x[1],reverse=True) #根据概率排序
    return rank

if __name__ == "__main__":
    N = 100
    step = 10 
    epsilon = 0.01 
    var_num = 2 
    x = [0,0] 
    nu = 10 
    #global_optimization(N, step, epsilon, var_num, x, nu)

    G = {'A' : {'a' : 1, 'c' : 1},  
         'B' : {'a' : 1, 'b' : 1, 'c':1, 'd':1},  
         'C' : {'c' : 1, 'd' : 1},  
         'a' : {'A' : 1, 'B' : 1},  
         'b' : {'B' : 1},  
         'c' : {'A' : 1, 'B' : 1, 'C':1},  
         'd' : {'B' : 1, 'C' : 1}}
    alpha = 0.85
    root = 'A'
    n = 500
    rank = personalRank(G, alpha, root, n)
    print(rank)
    
