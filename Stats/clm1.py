#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

# Define functions
def cumulative(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

# Set data
max_weight = float(input())
n = float(input())
mean = float(input())
std = float(input())

new_mean = mean * n
new_std = math.sqrt(n) * std

# Gets the result and show on the screen
print (round(cumulative(new_mean, new_std, max_weight),4))


# In[ ]:




