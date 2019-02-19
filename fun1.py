#!/usr/bin/env python
# coding: utf-8

# In[31]:


#Упржнение 2.4 (fun1.py)
x = int(input("Введите число:\n"))

def fun1(x):
    if -2.4 <= x <= 5.7:
        return x**2
    else:
        return 4
fun1(x)