# Задача 1.
# Создайте текстовый файл (шаблон), содержащий следующее:
# «Приветствую тебя, {{ user_name }}! Очень рад тебя видеть! С нашей
# последней встречи прошло {{ time }} лет… Прими этот {{ item }} и
# садись {{ place }}»
# Ваша программа во время запуска должна запросить соответствующие
# данные у пользователя через консоль. Затем заполнить данный шаблон этими
# данными и вывести отрендеренный текст в консоль.
# Дополнительно:
# Подготовьте файл ответов в формате json. При наличии этого файла
# программа не будет запрашивать у пользователя данные, а должная считать их
# из этого файла.

from jinja2 import Template
import os.path
import json


if os.path.isfile('#1/Ответы.json'):
    with open('#1/Ответы.json', mode='r', encoding='utf-8') as json_infile:
        answers = json.load(json_infile)
        for el in answers['Ответы']:
            user_name = el["Имя"]
            time = el["Срок"]
            item = el["Предмет"]
            place = el["Место"]
else:
    user_name = input("Имя: ")
    time = input("Срок: ")
    item = input("Предмет: ")
    place = input("Место: ")


with open('#1/шаблон.txt', 'r', encoding='utf-8') as txt_infile:
    tm = Template(txt_infile.read())

print(tm.render(user_name=user_name, time=time, item=item, place=place))
