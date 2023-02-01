# Задача 2.
# Даны два файла (в Moodle) формата csv и json, содержащие разные
# списки городов, их население, регион и индекс. Данные из файлов необходимо
# соединить таким образом, чтобы они содержали только уникальные значения.
# Для этого создайте класс City, у которого будут реализованы методы __hash__
# и __er__. Поместите экземпляры класса в коллекцию, при правильно
# реализованных вышеуказанных методов коллекция будет содержать только
# уникальные города.
# Новый список городов необходимо сохранить в форматы CSV и JSON.
# Используйте собственные функции преобразований.
# Дополнительно:
# Перед сохранением данных в файл отсортируйте список по численности
# населения. 

import csv
import json

class City:
    def __init__(self, население, регион, индекс, название, типРегиона):
        try:
            self.население = int(население)
        except ValueError:
            self.население = 0
        self.регион = регион
        self.индекс = int(индекс)
        self.название = название
        self.типРегиона = типРегиона

    def __eq__(self, other):
        return self.индекс == other.индекс

    def __hash__(self):
        return self.индекс



def sort_key(s):
    return s.население


def createJsonFile(cities_list):
    data = {}
    data['cities'] = []

    for city in cities_list:
        data['cities'].append({
            "Индекс": city.индекс,
            "Тип региона":  city.типРегиона,
            "Регион": city.регион,
            "Город": city.название,
            "Население": city.население,
        })

    with open('#2/Общий список.json', mode='w', encoding='utf-8') as json_outfile:
        json_outfile.write(json.dumps(data, ensure_ascii=False))


def createCsvFile(cities_list):
    with open('#2/Общий список.csv', mode='w', encoding='utf-8') as csv_outfile:
        file_writer = csv.writer(
            csv_outfile, delimiter=",", lineterminator="\r")

        file_writer.writerow(
            ["Индекс", "Тип региона", "Регион", "Город", "Население"])

        for city in cities_list:
            file_writer.writerow(
                [city.индекс, city.типРегиона, city.регион, city.название, city.население])



cities_set = set()

with open('#2/Города.json', mode='r', encoding='utf-8') as json_infile:
    cities = json.load(json_infile)
    for city in cities['data']:
        cities_set.add(City(
            city["Население"], city["Регион"], city["Индекс"], city["Город"], city["Тип региона"]))

with open('#2/Города.csv', mode='r', encoding='utf-8') as csv_infile:   
    count = 0
    for row in csv.reader(csv_infile, delimiter=","):
        if count > 0:
            cities_set.add(
                City(row[4], row[2], row[0], row[3], row[1]))
        count += 1


createCsvFile(sorted(cities_set, key=sort_key))
createJsonFile(sorted(cities_set, key=sort_key))