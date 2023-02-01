# Задача 1.
# Создайте класс, который при инициализации принимает параметр «путь
# до файла». Если файл не существует (проверка с помощью модуля os), то его
# необходимо создать при инициализации объекта данного класса. В атрибут
# words должен быть помещен список всех слов из текста. У класса должны быть
# следующие методы:
# 1) delete_word – должен удалить слово, которое было передано в вызов
# данного метода.
# 2) update_source – сохраняет все слова обратно в файл.
# Дополнительно:
# Добавить метод delete_char, который удаляет переданный символ из всех
# слов списка words.

import os.path

class MyClass():
    words = []
    directory: str

    def __init__(self, directory):
        self.directory = directory
        if os.path.isfile(self.directory):
            with open(self.directory, mode='r', encoding='utf-8') as fin:
                strings = fin.read().splitlines()
                for el in strings:
                    self.words+=(el.split(' '))
        else:
            print('Файл не найден')

    def delete_word(self, word):
        if word in self.words:
            self.words.remove(word)
    
    def update_source(self):
        if os.path.isfile(self.directory):
            with open(self.directory, mode='w', encoding='utf-8') as fout:
                fout.write(' '.join(self.words))
        else:
            print('Файл не найден')

    def delete_char(self, symbol):
        temp = []
        for el in self.words:
            temp.append(el.replace(symbol, ''))
        self.words = temp


msg = MyClass("#1/text.txt")
print(' '.join(msg.words))
msg.delete_word('для')
print(' '.join(msg.words))
msg.update_source()
msg.delete_char('а')
print(' '.join(msg.words))
msg.update_source()
