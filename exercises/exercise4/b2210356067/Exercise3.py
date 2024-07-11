#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

ran_num = random.randint(1,25)

while True:
    number = int(input("Enter a number between 1 and 25:"))

    if (number > ran_num):
        print("Decrease the number.")

    elif(number < ran_num):
        print("Increase the number.")
    else:
        print("The number you entered is correct.")
        break

