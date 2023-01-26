# Задача 9.
# Написать функцию, которая возвращает случайную дату в следующем
# формате «дд-мм-гггг».


import time
import random

print(time.strftime('%d-%m-%Y', time.localtime(random.randint(0, 1000000000))))
print(time.strftime('%d-%m-%Y', time.localtime(random.randint(0, 1000000000))))
print(time.strftime('%d-%m-%Y', time.localtime(random.randint(0, 1000000000))))
print(time.strftime('%d-%m-%Y', time.localtime(random.randint(0, 1000000000))))
print(time.strftime('%d-%m-%Y', time.localtime(random.randint(0, 1000000000))))
print(time.strftime('%d-%m-%Y', time.localtime(random.randint(0, 1000000000))))
