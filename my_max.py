#!/usr/bin/env python
# coding: utf-8

# In[19]:


#Упржнение 2.2 (my_max.py)
x = int(input("Введите число 1:\n"))
y = int(input("Введите число 2:\n"))

def max1(x,y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return print('Числа одинаковые')
max1(x,y)