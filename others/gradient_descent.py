# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 16:48:08 2018

@author: 祝超
"""

import numpy as np
import matplotlib.pyplot as plt
import random

def load_data():
    x_train = np.array([[1.1,1.5],[1.3,1.9],[1.5,2.3],[1.7,2.7],[1.9,3.1],
               [2.1,3.5],[2.3,3.9],[2.5,4.3],[2.7,4.7],[2.9,5.1]])
    y_train = np.array([[2.5], [3.2], [3.9], [4.6], [5.3], [6], [6.7], [7.4], [8.1], [8.8]])
    return x_train,y_train

def load_test_data():
    x_test = np.array([[3.1,5.5],[3.3,5.9],[3.5,6.3],[3.7,6.7],[3.9,7.1]])
    y_test = np.array([[9.5], [10.2], [10.9], [11.6], [12.3]])
    return x_test,y_test

def BGD(x, y, theta, alpha, m, max_iter):
    x_train = x.transpose()
    p = []
    for i in range(max_iter):
        pred = np.dot(x, theta)
        loss = pred - y
        p.append(np.sum(loss))
        gradient = np.dot(x_train, loss)/m #求导进行梯度下降计算
        #print('gradient = ', gradient, '\nloss =', loss)
        theta = theta - alpha * gradient
    plt.plot(p)
    plt.xlabel('iter')
    plt.ylabel('loss')
    return theta

def SGD(x, y, theta, alpha, m, max_iter):
    x_train = x.transpose()
    p = []
    q = []
    for i in range(max_iter):
        index = np.random.randint(x.shape[0])
        pred = np.dot(x,theta)
        loss = pred[index] -y[index]
        p.append(loss)
        gradient = x_train[:,index]*loss
        theta = theta - (alpha * gradient).reshape(theta.shape)
    plt.plot(p)
    plt.xlabel('iter')
    plt.ylabel('loss')
    return theta


def mini_BGD(x, y, theta, alpha, m, max_iter, batch_size):
    x_train = x.transpose()
    p = []
    for i in range(max_iter):
        pred = np.dot(x, theta)
        loss = pred - y
        data = np.zeros((x.shape[0],x.shape[1] + loss.shape[1] + y.shape[1]))
        data[:,0:2] = x
        data[:,2] = y.reshape(x.shape[0])
        data[:,3] = loss.reshape(x.shape[0])
        sample = np.random.permutation(data)[0:batch_size]
        p.append(np.sum(loss))
        gradient = np.dot(sample[:,0:2].T, sample[:,3].reshape(batch_size,1))/batch_size #求导进行梯度下降计算
        #print('gradient = ', gradient, '\nloss =', loss)
        theta = theta - alpha * gradient
    plt.plot(p)
    plt.xlabel('iter')
    plt.ylabel('loss')
    return theta

def prediction(x, theta):
    pred = np.dot(x, theta)
    print('pred = ',pred)
    return pred

def main():
    x, y = load_data()
    x_test, y_test = load_test_data()
    x_shape = np.shape(x)
    theta = np.zeros((x_shape[1],1))
    alpha = 0.01
    max_iter = 5000
    m = x_shape[0]
    batch_size = 5
    #theta = BGD(x, y, theta, alpha, m, max_iter)
    theta = mini_BGD(x, y, theta, alpha, m, max_iter, batch_size)
    print('theta = ',theta)
    prediction(x_test, theta)
    
if __name__ == "__main__":
    main()