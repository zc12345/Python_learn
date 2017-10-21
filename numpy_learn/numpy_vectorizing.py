import numpy as np
import time

#a = np.array([1,2,3,4])
#print(a)
a = np.random.rand(100000)
b = np.random.rand(100000)

tic = time.time()
c1 = np.dot(a,b)
toc = time.time()

print("vectorized version:"+str(1000*(toc-tic))+"ms")
print("result = %s"%c1)

tic1 = time.time()
c = 0
for i in range(100000):
    c += a[i]*b[i]
toc1 = time.time()

print("non-vectorized version:"+str(1000*(toc1-tic1))+"ms")
print("result = %s"%c)
