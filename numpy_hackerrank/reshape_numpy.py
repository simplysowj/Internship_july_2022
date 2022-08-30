#!/usr/bin/env python
# coding: utf-8

# Task
# 
# You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.

# In[3]:


import numpy


my_array=input().split()
my_array1=numpy.array(my_array,int)
print(numpy.reshape(my_array1,(3,3)))


# In[ ]:




