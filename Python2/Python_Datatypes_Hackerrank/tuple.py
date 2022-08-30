#!/usr/bin/env python
# coding: utf-8

# Task:
#        Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).

# In[7]:


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tuple_1=tuple((integer_list))
    print(hash(tuple_1))


# In[ ]:




