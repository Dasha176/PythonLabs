# Задача 12.
# Написать программу, которая переведет введенное пользователем число
# от -5 до 5 в значение словами. Например, «минус один»
# Дополнительно необходимо проверить введенное пользователем число.

while True:
    integer = int(input('Введите целое число от -5 до 5: '))
    if integer >= -5 and integer <= 5:
        break
    print('Число вне заданного диапазона')

if integer == -5:
    print('минус пять')
elif integer == -4:
    print('минус четыре')
elif integer == -3:
    print('минус три')
elif integer == -2:
    print('минус два')
elif integer == -1:
    print('минус один')
elif integer == 0:
    print('ноль')
elif integer == 1:
    print('один')
elif integer == 2:
    print('два')
elif integer == 3:
    print('три')
elif integer == 4:
    print('четыре')
else:
    print('пять')

