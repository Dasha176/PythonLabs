# Задача 3. Инкапсуляция (сокрытие доступа)
# Создайте класс Triangle (треугольник). Атрибуты, хранящие величину
# длины сторон треугольника, не должны быть доступны для чтения вне класса.
# При создании экземпляра класса в метод __init__ должны передаваться
# величины, соответствующие длинам сторон треугольника. Проверку
# устанавливаемых величин в данном методе делать не обязательно.
# Создайте отдельный метод на изменение каждого скрытого атрибута с
# проверкой присеваемого значения на соответствие правилу треугольника:
# длина одной стороны не должна превышать сумму длин остальных сторон.
# Создайте метод get_perimetr, который возвращает длину периметра.
# Дополнительно:
# Для запрета смены величины атрибута длины стороны используйте
# метод __setattr__. Новую величину в соответствующем методе необходимо
# задавать так: super().__setattr__(key, value).
# Пример будет доступен в дополнительных материалах к курсу.
# Создать еще один класс NewTriangle. Добиться возможности смотреть
# длину стороны вне класса, обращаясь к его атрибутам. Но изменять эти
# атрибуты должно быть возможно только внутри класса предназначенными для
# этого методами.

class Triangle:
    __a: int
    __b: int
    __c: int

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def set_sides(self, a, b, c):
        if (a < (self.__b + self.__c)) and (b < (self.__a + self.__c)) and (c < (self.__a + self.__b)):
            self.__a = a
            self.__b = b
            self.__c = c
        pass

    def get_perimetr(self):
        return self.__a + self.__b + self.__c
        

class NewTriangle():
    protected_attrs = ("a", "b", "c", "protected_attrs")

    def __init__(self, a, b, c):
        self.set_sides(a, b, c)
        pass

    def set_sides(self, a, b, c):
        super().__setattr__('a', a)
        super().__setattr__('b', b)
        super().__setattr__('c', c)
        pass

    def __setattr__(self, key, value):
        if key in self.protected_attrs:
            raise AttributeError(f"Нельзя установить данный атрибут {key}")
        super().__setattr__(key, value)


triangle = Triangle(2, 1, 7)
print(f'Длина периметра: {triangle.get_perimetr()}')

newTriangle = NewTriangle(6, 1, 9)