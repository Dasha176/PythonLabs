# Задача 2.
# Программа должна запросить у пользователя следующую информацию:
# 1) имена двух персонажей;
# 2) вид соревнования;
# 3) характеристики персонажей в данном виде деятельности.
# Подготовьте шаблон, в который при рендеринге передастся полученная
# информация. В результате рендеринга должен быть получен текст,
# содержащий имя победителя (побеждает тот, чьи характеристики больше).
# При равенстве вывести соответствующею информацию Сравнение
# характеристик должно происходить в блоке if шаблонизатора.
# Дополнительно:
# Вывод на экран должен быть в формате json или csv. Оба формата
# должны содержать следующие поля:
# 1) имя победителя
# 2) его характеристики
# 3) вид соревнования
# 4) дата проведения соревнования
# Имена полей произвольные.

import os.path
from jinja2 import Template
import json


class Char:
    def __init__(self, имя, тип_соревнования, характеристика, дата_соревнования):
        self.имя = имя
        self.тип_соревнования = тип_соревнования
        self.характеристика = характеристика
        self.дата_соревнования = дата_соревнования


def createJsonFile(characters):
    data = {}
    data['Characters'] = []

    for el in characters:
        data['Characters'].append({
            "Имя победителя": el.имя,
            "Вид соревнования":  el.тип_соревнования,
            "Дата соревнования": el.дата_соревнования,
            "Характеристика": el.характеристика,
        })

    with open('#2/Персонажи.json', 'w', encoding='utf-8') as json_outfile:
        json_outfile.write(json.dumps(data, ensure_ascii=False))



characters = []
for i in range(0, 2):
    characters.append(Char(input("Имя: "), input("Вид соревнования: "), int(input("Характеристика: ")), input("Дата соревнования: ")))
    print()


if os.path.isfile('#2/шаблон.txt'):
    with open('#2/шаблон.txt', "r", encoding='utf-8') as txt_infile:
        tm = Template(txt_infile.read())
else:
    print("Файл не найден")

print('\n', tm.render(
    competition=characters[0].тип_соревнования, first=characters[0], second=characters[1]))


createJsonFile(characters)

with open('#2/Персонажи.json', 'r', encoding='utf-8') as json_outfile:
    print(json_outfile.read())