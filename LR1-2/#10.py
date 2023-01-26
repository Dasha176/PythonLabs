# Задача 10.
# Написать функцию, которая принимает:
# 1) 1 обязательный аргумент дату в формате строки (можно использовать
# функцию из задачи №9)
# 2) 1 необязательный аргумент объект даты, по умолчанию должна быть
# текущая дата
# Функция должна вернуть число секунд между двумя этими датами.


import time as t

def dateDifference(date1, date2=t.strftime("%d-%m-%Y", t.localtime())):
    return abs(t.mktime(t.strptime(date2, "%d-%m-%Y")) - t.mktime(t.strptime(date1, "%d-%m-%Y")))


print(dateDifference("26-01-2023"))
print(dateDifference("01-01-2022", "01-01-2022"))
print(dateDifference("01-01-2022", "02-01-2022"))
