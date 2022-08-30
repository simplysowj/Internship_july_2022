#!/usr/bin/env python
# coding: utf-8

# CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).
# 
# Specifications of HEX Color Code
# 
# ■ It must start with a '#' symbol.
# ■ It can have 3 or 6 digits.
# ■ Each digit is in the range of 0 to F. (1,2,3,4,5,6,7,8,9,0,A,B,C,D,E,F)
# Examples
# 
# Valid Hex Color Codes
# #FFF 
# #025 
# #F0A1FB 
# 
# Invalid Hex Color Codes
# #fffabg
# #abcf
# #12365erff

# In[1]:


import re
n = int(input())
for t in range(n):
    s = input()
    match_result = re.findall(r'(#[0-9A-Fa-f]{3}|#[0-9A-Fa-f]{6})(?:[;,.)]{1})',s)
    for i in match_result:
        if i != '':
            print(i)


# Explanation
# 
# #BED and #Cab satisfy the Hex Color Code criteria, but they are used as selectors and not as color codes in the given CSS.
# 
# Hence, the valid color codes are:
# 
# #FfFdF8
# #aef
# #f9f9f9
# #fff
# #ABC
# #fff
# 
# Note: There are no comments ( // or /* */) in CSS Code.

# In[ ]:




