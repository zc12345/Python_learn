import matplotlib.pyplot as plt
import numpy as np

def valentine():
    '''
    draw a heart-style pic
    '''
    t = np.arange(np.pi, 3*np.pi, 0.1)
    #x = 16*np.sin(t)**3
    #y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

    plt.figure(figsize = (8,6), dpi = 80, facecolor = 'white')
    plt.axis('off')
    for i in t:
        xi = 16*np.sin(i)**3
        yi = 13*np.cos(i) - 5*np.cos(2*i) - 2*np.cos(3*i) - np.cos(4*i)
        plt.pause(0.02)
        plt.plot(xi, yi, 'r*', color = 'red')
    #plt.plot(x, y, 'r*',color = 'red')
    plt.axis('off')
    #plt.fill(x, y, 'hotpink')
    plt.text(0, -0.4, 'Valentine\'s Day', fontsize = 20, fontweight = 'bold',
             color = 'black', horizontalalignment = 'center')
    plt.show()

def factorial1(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial2(n):
    result = 1
    for i in range(n):
        result *= i + 1
    return result

def factorial3(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial3(n-1)

def fib1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

def fib2(n):
    f1 = 1
    f2 = 1
    f3 = 1
    if n < 1:
        return -1
    while n > 2:
        f3 = f2 + f1
        f1 = f2
        f2 = f3
        n -= 1
    return f3

def fib3(n):
    fib = [1, 1]
    if n < 1:
        return -1
    for i in range(2, n):
        f = fib[i-1] + fib[i-2]
        fib.append(f)
    print(fib)
    return fib[n-1]

def hanoi(n, x, y, z):
    if n == 1:
        print('%s --> %s'%(x, z))
    else:
        hanoi(n-1, x, z, y)
        print('%s --> %s'%(x, z))
        hanoi(n-1, y, x, z)

if __name__ == "__main__":
    n = int(input("input an integer:"))
    res = hanoi(n, 'x', 'y', 'z')
    print("hanoi %s  = %s" % (n, res))
    valentine()
