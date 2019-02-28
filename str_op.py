#Упражнение 4.2 (str_op.py)

s = "У лукоморья 123 дуб зеленый 456"
#1
print('1)', s.index('я'))

#2
print('2)', s.count('у'))

#3
if s.isalpha() == False:
    print('3)', s.upper())
else:
    print('3)')
    
#4
if len(s) > 4:
    print('4)', s.lower())
else:
    print('4)')
    
#5
print('4)', s.replace(s[0], 'О'))