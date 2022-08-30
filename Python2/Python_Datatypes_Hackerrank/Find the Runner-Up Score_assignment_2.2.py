#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

#Input Format

#The first line contains n. The second line contains an array of n integers each separated by a space.


# In[3]:


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=sorted(arr,reverse=True)
    for i in range(len(arr)):
        if(arr[0]==arr[i]):
            continue
        else:
            print(arr[i])
            break
            


# In[ ]:




