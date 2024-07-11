#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
try:
    two_point = int(sys.argv[1]) * 2 
    three_point = int(sys.argv[2]) * 3 
    single_point = int(sys.argv[3])

    overall_score = two_point + three_point + single_point

    print(overall_score)
    
except:
    pass


# In[2]:


def healthStatus(height ,mass):
    BMI = mass / (height**2)
    if BMI >= 30:
        return "You are obese!"
    elif BMI >= 24.9 and BMI <30:
        return "You are overweight!"
    elif BMI >= 18.5 and BMI <24.9:
        return "You are healthy!"
    else:
        return "You are underweight!"

#2210356067 - Gökdeniz Şİmşek

