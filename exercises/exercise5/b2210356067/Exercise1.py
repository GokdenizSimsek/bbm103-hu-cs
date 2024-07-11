#!/usr/bin/env python
# coding: utf-8

# In[6]:


Number = int(input("Enter the Number N value:"))
dic_num = {}

for x in range(1,Number+1):
    dic_num[x] = list(x*"*")
print(dic_num)

