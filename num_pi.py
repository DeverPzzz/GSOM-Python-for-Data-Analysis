#Упражнение 4.1 (num_pi.py)

n = int(input('Сколько знаков после запятой? '))
def func1(n):
    import math
    str1='{pi:.' + str(n) + 'f}'
    return float(str1.format(pi = math.pi))
func1(n)