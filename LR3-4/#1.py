# Задача 1. Полиморфизм:
# Создать классы Cat, Dog и Chicken. Для каждого класса создать метод
# get_sound и атрибут name.
# При обращении к атрибуту name должна возвращаться строка,
# содержащая кличку питомца.
# При вызове метода get_sound в зависимости от класса в консоль должен
# выводиться следующий текст:
# «мяю» - для Cat,
# «гав-гав» - для Dog,
# «чик-чик» - для Chicken.
# Создайте список Animals, содержащий не менее 3х экземпляров каждого
# класса. Затем создайте цикл, в котором у каждого элемента списка будет
# выведен на экран атрибут name и вызван метод get_sound.
# Для каждого класса создать метод add_friend, при вызове данного
# метода, ему должен аргументом передаться любой объект. Переданный объект
# должен расширить список «друзей» экземпляра класса, являющимся
# атрибутом friends.
# Дополнительно:
# В методе add_friend должна осуществляться проверка добавляемого
# объекта. Каждый класс может иметь в «друзьях» не более 2х типов объектов и
# не более пяти экземпляров в общей сумме. То есть, для класса должны быть
# определены два типа объектов, которых можно добавить в список, и суммарно
# в этом списке может быть не более пяти элементов.
# Реализовать метод «список друзей» для каждого класса: на экран
# выводится имя каждого элемента списка или сообщение о пустоте списка.

class Cat():
    name: str
    friends = []
    friends_types = 0

    def __getattribute__(self, item):
        if item == 'name':
            return 'Кличка питомца: ' + object.__getattribute__(self, item)
        else:
            return object.__getattribute__(self, item)
    
    def get_sound(self):
        print('мяу')
        pass

    def friends_list(self):
        if len(self.friends) == 0:
            print("Список пуст")
        else:
            for el in self.friends:
                print(el.name)

    def add_friend(self, friend):
        if isinstance(Cat(), Cat) or isinstance(Dog(), Dog) or isinstance(Chicken(), Chicken):
            if len(self.friends) < 5:
                boolVar = False

                for el in self.friends:
                    if type(el) == type(friend):
                        boolVar = True     
                
                if boolVar == False:
                    self.friends_types += 1
                
                if self.friends_types < 3:
                    self.friends.append(friend)
        pass


class Dog():
    name: str
    friends = []
    friends_types = 0

    def __setattr__(self, key, value):
        if key == 'name':
            object.__setattr__(self, key, value)

    def __getattribute__(self, item):
        if item == 'name':
            return 'Кличка питомца: ' + object.__getattribute__(self, item)
        else:
            return object.__getattribute__(self, item)
    
    def get_sound(self):
        print('гав-гав')
        pass

    def friends_list(self):
        if len(self.friends) == 0:
            print("Список пуст")
        else:
            for el in self.friends:
                print(el.name)

    def add_friend(self, friend):
        if isinstance(Cat(), Cat) or isinstance(Dog(), Dog) or isinstance(Chicken(), Chicken):
            if len(self.friends) < 5:
                boolVar = False

                for el in self.friends:
                    if type(el) == type(friend):
                        boolVar = True     
                
                if boolVar == False:
                    self.friends_types += 1
                
                if self.friends_types < 3:
                    self.friends.append(friend)
        pass


class Chicken():
    name: str
    friends = []
    friends_types = 0

    def __getattribute__(self, item):
        if item == 'name':
            return 'Кличка питомца: ' + object.__getattribute__(self, item)
        else:
            return object.__getattribute__(self, item)
    
    def get_sound(self):
        print('чик-чик')
        pass

    def friends_list(self):
        if len(self.friends) == 0:
            print("Список пуст")
        else:
            for el in self.friends:
                print(el.name)

    def add_friend(self, friend):
        if isinstance(Cat(), Cat) or isinstance(Dog(), Dog) or isinstance(Chicken(), Chicken):
            if len(self.friends) < 5:
                boolVar = False

                for el in self.friends:
                    if type(el) == type(friend):
                        boolVar = True     
                
                if boolVar == False:
                    self.friends_types += 1
                
                if self.friends_types < 3:
                    self.friends.append(friend)
        pass




animals = [Cat(), Dog(), Chicken()]

animals[0].name = 'Том'
animals[1].name = 'Дружок'
animals[2].name = 'Ряба'

for el in animals:
    print(el.name)
    el.get_sound()  

animals[0].add_friend(animals[0])
animals[0].add_friend(animals[0])
animals[0].add_friend(animals[2])
animals[0].add_friend(animals[0])
animals[0].add_friend(animals[1])
animals[0].add_friend(animals[2])

animals[0].friends_list()


