#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

# Set data
n = float(input())
mean = float(input())
std = float(input())
percent_ci = float(input())
value_ci = float(input())

# Formula CI
ci = value_ci * (std / math.sqrt(n))

# Gets the result and show on the screen
print(round(mean - ci, 2))
print(round(mean + ci, 2))


# In[ ]:




