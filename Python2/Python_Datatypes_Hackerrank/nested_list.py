#!/usr/bin/env python
# coding: utf-8

# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# In[6]:


if __name__ == '__main__':
    students = []
    scores = []
    for N in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        students.append([name, score])
    
        
    count = scores.count(min(scores))
    for i in range(count):
        scores.remove(min(scores))
        
    secondHigh = min(scores)
    
    students.sort()
    
    output = [x for x in students if x[1] == secondHigh]
    
    for i in output:
        
            print(i[0])
      
            
        


# #### 
