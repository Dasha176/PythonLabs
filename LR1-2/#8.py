# Задача 8.
# Написать программу, которая запрашивает у пользователя целое число
# больше 5. Так же программа должна сгенерировать число от 0 до 5. Оба числа
# должны быть переданы в функцию, созданную в задаче №6. На экран должен
# быть выведен результат работы функции.
# Дополнительно необходимо проверить введенное пользователем число.


def myFunc(a, b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        if a > 0 and b > 0:
            return a * b
        else:
            print('Аргумент не положительный')
    else:
        print('Аргумент не числовой')


while True:
    myInteger = int(input('Введите целое число больше пяти: '))
    if myInteger > 5:
        break
    print('Число не больше пяти')

import random
randomInteger = random.randint(0, 5)
print('Рандомное число от 0 до 5: ', randomInteger)

print('Результат перемножения:', myFunc(myInteger, randomInteger))