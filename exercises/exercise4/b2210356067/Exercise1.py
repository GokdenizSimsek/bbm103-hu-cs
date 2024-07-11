#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N = int(input("Enter the number:"))
list1 = list(range(1,N+1))
sum_oddnum = 0 
sum_evennum = 0
num_evennum = 0

if N == 1:
    sum_oddnum = 1
    ave_num = 0
elif N > 0:
    for a in list1:
        if a % 2 == 0:
            sum_evennum += a
            num_evennum += 1
        else:
            sum_oddnum += a
    ave_num = sum_evennum/num_evennum
print("The sum of odd numbers is:", sum_oddnum)
print("The average of even numbers is:", ave_num)

