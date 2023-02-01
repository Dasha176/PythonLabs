# Задача 3.
# В прошлой работе Вы получили список городов в формате json или csv.
# Необходимо сделать шаблон в формате html. Шаблон необходимо заполнить
# данными из Ваших файлов и сохранить как result.html.
# «добавление стилей в самом html документе или подключение файла css
# для более приятного отображения – приветствуется»
# Дополнительно:
# Ваша программа должна перед рендерингом запросить наименьшее
# количество население города для помещения его в шаблон. То есть города, чье
# население ниже установленной планки не должны присутствовать в
# result.html. Фильтрация должна быть в заложена в шаблон.

from jinja2 import Template
import csv
import os.path

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


# Получение списка городов в формате csv
cities_list = list()

with open('#3/Общий список.csv', mode='r', encoding='utf-8') as csv_infile:   
    count = 0
    for row in csv.reader(csv_infile, delimiter=","):
        if count > 0:
            cities_list.append(
                City(row[4], row[2], row[0], row[3], row[1]))
        count += 1

# Считывание шаблона
if os.path.isfile('#3/шаблон.txt'):
    with open('#3/шаблон.txt', "r", encoding='utf-8') as txt_infile:
        tm = Template(txt_infile.read())
else:
    print("Файл не найден")

# Запрос наименьшего населения
smallestPopulation = int(input("Предел населения: "))

# Генерация веб-страницы
with open('#3/result.html', 'w', encoding='utf-8') as html_page:
    html_page.write(tm.render(cities=cities_list, smallest_population=smallestPopulation))