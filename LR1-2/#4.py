# Задача 4.
# Написать программу, которая запрашивает у пользователя
# положительное целое число. Программа должна вывести на экран квадраты
# чисел от 1 до введенного числа.
# Дополнительно необходимо проверить введенные пользователем
# данные.

integer = int(input("Введите положительное целое число: "))
i = 1

while i*i <= integer:
    print(i*i, end=', ')
    i += 1

 