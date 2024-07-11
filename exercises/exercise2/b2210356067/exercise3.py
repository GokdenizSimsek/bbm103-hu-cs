#!/usr/bin/env python
# coding: utf-8

# In[ ]:


b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))
delta = b**2 - 4*c
root_1 = (-b + delta**0.5)/2
root_2 = (-b - delta**0.5)/2
print("The roots of the equaiton are {} and {}".format(root_1,root_2))

