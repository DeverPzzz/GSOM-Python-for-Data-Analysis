#Упражнение 6.1 (interval_fun)

lst = []

def func1(x):
    return x**2 + 3

for i in range (10,30,2): #учитывал интервал от 10 до 30 (не включительно)
    lst.append(func1(i))

sum(lst)