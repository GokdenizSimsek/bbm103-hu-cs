#!/usr/bin/env python
# coding: utf-8

# In[1]:


Number1 = int(input("Enter the Number nth largest element:"))
my_list = [1000, 298, 3579, 100, 200, -45, 900]
my_list.sort()
nth_larg = my_list[Number1-1]
print(nth_larg)


# In[ ]:




