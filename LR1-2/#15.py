# Задача 15.
# Написать функцию, которая примет произвольную строку. Функция
# должна вернуть словарь, который содержит себе следующие ключи и
# значения:
# 1) length — длина строки
# 2) words_count — количество слов
# 3) digit_count — количество цифровых символов


def myFunc(stroka):
    wordsQuantity = len(stroka.split(' '))
    numsQuantity = 0

    for el in stroka:
        if el.isdigit():
            numsQuantity += 1

    return {'Длина строки': len(stroka), 'Количество слов': wordsQuantity, 'Количество чисел': numsQuantity}


dictionary = myFunc(input("Введите строку: "))

for el in dictionary.keys():
    print(el, ':', dictionary[el])
