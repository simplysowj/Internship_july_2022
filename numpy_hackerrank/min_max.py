#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
initial = list(map(int, input().split()))
array = []
for _ in range(initial[0]):
    array.append(list(map(int, input().split())))
min_list = list(numpy.min(array, axis = 1))
print(max(min_list))


# In[ ]:




