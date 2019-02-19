#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Упржнение 2.1 (table.py)
n = int(input("Введите атомный номер элемента:\n"))

if n == 3:
    print("Li")
elif n == 25:
    print("Mn")
elif n == 80:
    print("Hg")
elif n == 17:
    print("Cl")
elif  n > 118 or n < 1:
    print("Что это?!")
else:
    print("Нету в базе")

