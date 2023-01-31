# Задача 1.
# Создайте 3 класса:
# 1) Point – точка на координатной плоскости, при создании экземпляра
# класса должны передаваться целочисленные значения обозначающие
# координаты x и y точки. Также точке должно передаваться ее имя.
# 2) Segment – отрезок, при создании должен принять два экземпляра
# класса Point. Учтите, имена точек и переменных для хранения их
# внутри класса никак не связаны.
# 3) BrokenLine – ломанная линия, при создании принимает список
# экземпляров Point. Список должен содержать не менее 3х точек.

class Point:
    name: str
    __x: int
    __y: int
    def __init__(self, name, x, y):
        self.name = name
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'{self.name}({self.__x},{self.__y})'

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y

    def __hash__(self):
        return hash(self.name)

    def __add__(self, other):
        if isinstance(other, Point):
            return Segment(self, other)
        elif isinstance(other, Segment):
            return BrokenLine([self, other.firstPoint, other.secondPoint])
        elif isinstance(other, BrokenLine):
            other.points.append(self)

    def set_coordinate(self, x, y):
        self.__x = x
        self.__y = y
        pass 

    def get_coordinate(self):
        return self.__x, self.__y


class Segment:
    firstPoint: Point
    secondPoint: Point
    x1: int
    y1: int
    x2: int
    y2: int

    def __init__(self, firstPoint, secondPoint):
        self.firstPoint = firstPoint
        self.secondPoint = secondPoint
        self.x1, self.y1 = self.firstPoint.get_coordinate()
        self.x2, self.y2 = self.secondPoint.get_coordinate()

    def get_len(self):
        return ((self.x1-self.x2)**2+(self.y1-self.y2)**2)**(1/2)

    def __str__(self):
        return f'{self.firstPoint.name}{self.secondPoint.name}({self.x1}, {self.y1}; {self.x2}, {self.y2})'

    def __add__(self, other):
        if isinstance(other, BrokenLine):
            other.points.append(self.firstPoint)
            other.points.append(self.secondPoint)            
        elif isinstance(other, Point):
            return BrokenLine([self.firstPoint, self.secondPoint, other])
        elif isinstance(other, Segment):
            if self.firstPoint == other.firstPoint or self.secondPoint == other.firstPoint:
                return BrokenLine([self.firstPoint, self.secondPoint, other.secondPoint])
            elif self.firstPoint == other.secondPoint or self.secondPoint == other.secondPoint:
                return BrokenLine([self.firstPoint, self.secondPoint, other.firstPoint])


class BrokenLine:
    points: list

    def __init__(self, points):
        # if(len(points) <= 3):
        self.points = points

    def get_len(self):
        lenght = 0
        for i in range(0, len(self.points) - 1):
            segment = Segment(self.points[i], self.points[i + 1])
            lenght += segment.get_len()
        return lenght

    def __str__(self):
        pointsNames = ''
        for el in self.points:
            pointsNames = pointsNames + el.name + ', '
        return  pointsNames

    def __add__(self, other):
        if isinstance(other, Point):
            if other not in self.points:
                self.points.append(other)
                return BrokenLine(self.points)