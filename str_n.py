#Упражнение 4.3 (str_n.py)

s = input("Введите строку: ")
n = int(input("Введите число: "))

def func1(s,n):
    if len(s) > n:
        return s.upper()
    else:
        return s
func1(s,n)

