# Задача 14.
# Написать функцию, которая принимает список строк. Функция должна
# вернуть случайный элемент списка в верхнем регистре.

import random as r

def myFunc(myStrList):
    return myStrList[r.randint(0, len(myStrList)-1)].upper()


myList = ['jjdjks', "ajjwk", 'x-files', "001-2", '2kk1j', "421"]

print(myFunc(myList))