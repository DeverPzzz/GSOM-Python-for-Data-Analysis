#Упражнение 6.2 (new_list)

lst = [2, 4, 9, 16, 25]

#1 с помощью функции for
lst1 = []
for i in lst:
    lst1.append(i**2)
print(lst1)

#2 с помощью функции map
def func1(x):
    return x**2
print(list(map(func1, lst)))

#3 с помощью генератора списков
lst2 = []
lst2 = [i**2 for i in lst]
print(lst2)