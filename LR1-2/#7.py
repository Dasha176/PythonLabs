# Задача 7.
# Написать функцию, принимающую 2 аргумента: 2 положительных
# числа. Функция должна возвращать результат перемножения данных чисел.

def myFunc(a, b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        if a > 0 and b > 0:
            return a * b
        else:
            print('Аргумент не положительный')
    else:
        print('Аргумент не числовой')


print(myFunc(1, 4))