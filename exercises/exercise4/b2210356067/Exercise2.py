#!/usr/bin/env python
# coding: utf-8

# In[ ]:


e_mail = str(input("Enter your e-mail address:"))

list2 = list(e_mail)
if "@" in list2 and "." in list2:
    print("Your e-mail address is a valid e-mail address.")
else:
    print("Your e-mail address is an invalid e-mail address.")

