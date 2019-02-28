#Упражнение 3.1

y = int(input("Введите число: "))

import random
x = random.randint(1,4)

if x == y:
    print ("Победа")
elif x > y:
    print("Больше введеного числа")
elif y > x:
    print("Меньше введеного числа")