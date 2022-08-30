#!/usr/bin/env python
# coding: utf-8

# In[ ]:


You are given a positive integer n .
Your task is to print a palindromic triangle of size n.


# In[1]:



for i in range(1,int(input())+1):
    
     print (((10**i - 1)//9)**2)


# In[ ]:




