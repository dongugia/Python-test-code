import timeit
normal_py_sec = timeit.timeit('sum(x*x for x in range(1000))', number=10000)
naive_np_sec = timeit.timeit('sum(na*na)',setup = "import numpy as np; na = np.arange(1000)", number= 10000)
good_np_sec = timeit.timeit('na.dot(na)',setup= "import numpy as np; na = np.arange(1000)", number= 10000)

print(" Normal Python : %f sec" %normal_py_sec)
print(" Navie Python : %f sec" %naive_np_sec)
print(" Good Python : %f sec" %good_np_sec)

import numpy as np

a = np.array([1,2,3])
print(a.dtype)

print(np.array(['1', "stringy"]).dtype)

print(np.array([1, "stringy" ,set([1,2,3])]).dtype)

