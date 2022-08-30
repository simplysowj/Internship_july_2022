#!/usr/bin/env python
# coding: utf-8

# Your task is to print the transpose and flatten results.

# In[1]:


import numpy
n,m = map(int,input().split())
ar = []
for i in range(n):
    row = list(map(int,input().split()))
    ar.append(row)
np_ar = numpy.array(ar)
print(numpy.transpose(np_ar))
print(np_ar.flatten())


# In[ ]:




