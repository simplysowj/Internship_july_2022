#!/usr/bin/env python
# coding: utf-8

# In[ ]:


You are given three integers: a,b , and m . Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).


# In[7]:


a=int(input("enter the value between 1 and 10   :"))
b=int(input("enter the value between 1 and 10   :"))
m=int(input("enter the 2 and 1000   :"))
if(1<=a<=10 and 1<=b<=10):
    print(pow(a,b))
else:
    print("enter the value between 1 and 10")
    
if(2<=m<=1000):
    print(pow(a,b,m))
else:
    print("enter the value between 2 and 1000")
    


# In[ ]:




