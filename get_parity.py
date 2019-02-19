#!/usr/bin/env python
# coding: utf-8

# In[25]:


#Упржнение 2.3 (get_parity.py)
x = int(input("Введите число, которое хотите проверить на четность:\n"))

def Chotnoe(x):
    if x % 2 == 0:
        return print('Четное')
    else:
        return print('Нечетное')
Chotnoe(x)