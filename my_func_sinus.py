#Упражнение 3.2

x = float(input("Введите число: "))
def func1(x):
    import math
    if 0.2 <= x <= 0.9:
        print(math.sin(x))
    else:
        print(1)
func1(x)



