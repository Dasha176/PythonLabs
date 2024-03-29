# Задача 2. Работа с классом Point
# Определить метод приведения к строке (__str__) таким образом, чтобы
# возвращалась строка следующего формата:
# {Имя точки}({координата x},{координата y}) , пример А(3,4)
# Определить метод сравнения (__eq__) и уникальности (__hash__) для
# точки. Продемонстрировать работу методов путем сравнения двух
# экземпляров и создания коллекции (set) экземпляров длинною не менее 5 шт.
# Добавить метод сложения (__add__). При сложении двух точек должен
# возвращаться новый экземпляр класса Segment.
# Дополнительно:
# 1) при сложении с классом Segment должен возвращаться экземпляр
# класса BrokenLine.
# 2) При сложении с классом BrokenLine, последний должен расширить
# свой список точек.
# 3) Скрыть от пользователя прямой доступ к атрибутам координат точек.
# Изменение координат реализовать через метод set_coordinate.
# Получение текущей координаты реализовать через метод
# get_coordinate.

import myClasses as myc 

a = myc.Point('A', 21, 0)
b = myc.Point('B', 0, 86)
c = myc.Point('C', 0, 86)
d = myc.Point('D', -5, 12)

print(a)
print(b)
print(c)
print('(A == B) ==', a == b)
print('(B == C) ==', b == c)

collection = { a, b, b, c, a, c }

for el in collection:
    print(el)

segment = a + b 
brokenLine = c + segment