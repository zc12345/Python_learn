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

if __name__ == "__main__":
    valentine()
