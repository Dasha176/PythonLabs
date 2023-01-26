# Задача 5.
# Написать программу, которая запрашивает у пользователя
# последовательность чисел (не более 10 шт.). Программа должна вывести
# введенные числа в порядке возрастания.

numbersList = []

for el in range(10):
    numbersList.append(int(input('Введите число №'+str(el+1)+': ')))

numbersList.sort()

print('Результат: ')
for el in numbersList:
    print(el, end=', ')