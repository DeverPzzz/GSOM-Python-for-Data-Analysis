#Упражнение 5.1 (random_letter1)

lst = ['самовар', 'весна', 'лето']

import random
lst1 = list(lst[random.randint(0, len(lst)-1)])

import copy
lst2 = copy.deepcopy(lst1)

n = random.randint(0, len(lst1)-1)
lst2[n] = '?'
print(''.join(lst2))

s = input('Введите букву: ')

if s.lower() == lst1[n]:
    print('\nПобеда!', '\nСлово: ' + ''.join(lst1))
else:
    print('\nУвы! Попробуйте в другой раз.', '\nСлово: ' + ''.join(lst1))

