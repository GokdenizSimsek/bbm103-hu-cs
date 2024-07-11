#!/usr/bin/env python
# coding: utf-8

# In[ ]:


number = int(input("Enter a number for convert to binary format:"))
binary_code = ("")
while number > 1:
    if number % 2 == 0:
        binary_code = "0" + binary_code
        number = number//2
    else:
        binary_code = "1" + binary_code
        number = number//2
binary_code = "1" + binary_code
print(binary_code)

