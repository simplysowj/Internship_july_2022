#!/usr/bin/env python
# coding: utf-8

# Consider a list (list = []). You can perform the following commands:
# 
#      1. insert i e: Insert integer e at position i.
#      2. print: Print the list.
#      3. remove e: Delete the first occurrence of integer e .
#      4. append e: Insert integer e at the end of the list. 
#      5. sort: Sort the list.
#      6. pop: Pop the last element from the list.
#      7. reverse: Reverse the list

# In[4]:


if __name__ == '__main__':
    N = int(input())
    list_1=[]
    for i in range(N):
        list_1.append(input().split())
    result=[]
    for i in range(N):
        if list_1[i][0]=='insert':
            result.insert(int(list_1[i][1]),int(list_1[i][2]))
        elif list_1[i][0]=='print':
            print(result)
        elif list_1[i][0]=='remove':
            print(list_1[i][1])
            result.remove(int(list_1[i][1]))
        elif list_1[i][0]=='append':
            result.append(int(list_1[i][1]))
        elif list_1[i][0]=='sort':
            result.sort()
        elif list_1[i][0]=='pop':
            result.pop()        
        elif list_1[i][0]=='reverse':
            result.reverse()
                        



# In[ ]:




