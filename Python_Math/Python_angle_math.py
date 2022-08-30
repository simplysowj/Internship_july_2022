#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

AB = int(input())
BC = int(input())

hypotenuse  = math.sqrt(AB**2 + BC**2)
hypotenuse  = hypotenuse /2.0
adj = BC/2.0

output = int(round(math.degrees(math.acos(adj/hypotenuse ))))

output = str(output)

print(output+u'\N{DEGREE SIGN}')


# In[ ]:




