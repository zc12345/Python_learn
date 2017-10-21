import numpy as np

a = np.random.rand(5)
#a = np.random.rand(1,5)
#a = np.random.rand(5,1)
a = a.reshape(5,1)
'''
print(a)
print(a.shape)
print(a.T)
print(np.dot(a, a.T))
'''

b = np.array([[56.0,0.0,4.4,68.0],
              [1.2,104.0,52.0,8.0],
              [1.8,135.0,99.0,0.9]])
b = b.reshape(12,1)
#print(b)

m1 = np.random.rand(2,3)
m2 = np.random.rand(2,1)
m3 = np.random.randn(4,3)
m4 = np.random.randn(3,2)
#c = m3 * m4 #error
c = np.dot(m3,m4)
#print((m1+m2).shape)
print(c.shape)
