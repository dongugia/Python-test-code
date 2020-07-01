import numpy as np
a = np.array([0,1,2,3,4,5])
print(a)
print(a.ndim)
print(a.shape)
b= a.reshape((3,2))
print(b)
print(b.ndim)
print(b.shape)
b [1][0] =  77
print(b)
print(a>4)
print(a)
print(a.clip(0,4))
a[a>4]=4
print(a)
c = np.array([1,2,np.NAN,3,4]) # let'spretend we have read this from a text file
print(c)
print(np.isnan(c))
print(c[~np.isnan(c)])
print(np.mean(c[~np.isnan(c)]))