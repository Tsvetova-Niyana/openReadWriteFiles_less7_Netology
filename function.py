import os
import json


def formation_dictionary_of_recipes():
    """Задача №1. Должен получится следующий словарь
    cook_book = {
        'Омлет': [
            {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
            {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
            {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
        ],
        'Утка по-пекински': [
            {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
            {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
            {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
            {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
        ],
        'Запеченный картофель': [
            {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
            {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
            {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
        ]
    }"""

    # Открытие файла с рецептами
    with open("recipes.txt", encoding='utf-8') as recipes:

        # формирование пустого словаря
        cook_book = {}

        #  формирование цикла для считывания данных
        for line in recipes:
            # выборка наименования рецепта (считываем первую строку)
            recipes_name = line.strip()
            # выборка количества используемых ингридиентов (считываем вторую строку)
            count = int(recipes.readline())

            # формирование списка под ингридиенты
            ingredients = []

            #  формирование цикла для считывания данных по количеству строк используемых ингридиентов
            for item in range(count):
                ingredient_info = recipes.readline().strip()

                #  распаковка данных при помощи метода split()
                ingredient_name, quantity, measure = ingredient_info.split(' | ')

                #  добавление данных в нужном формате в список при помощи метода append()
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })

            #  добавление данных в словарь (блюда и их ингридиенты)
            cook_book[recipes_name] = ingredients
            #  считывание пустой строки
            recipes.readline()

        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    """
    Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого
    мы будем готовить

    get_shop_list_by_dishes(dishes, person_count)
    На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например,
    для такого вызова

    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    Должен быть следующий результат:

    {
      'Картофель': {'measure': 'кг', 'quantity': 2},
      'Молоко': {'measure': 'мл', 'quantity': 200},
      'Помидор': {'measure': 'шт', 'quantity': 4},
      'Сыр гауда': {'measure': 'г', 'quantity': 200},
      'Яйцо': {'measure': 'шт', 'quantity': 4},
      'Чеснок': {'measure': 'зубч', 'quantity': 6}
    }
    Обратите внимание, что ингредиенты могут повторяться
    """
    cook_book = formation_dictionary_of_recipes()

    # формирование словаря под ингридиенты запрошенных блюд
    list_by_dishes = {}

    # формирование цикла для получения данных об ингридиентах
    for name in dishes:

        """ формируем запрос на получение информации, в случае если переданное название блюда 
            содержится в словаре с рецептами"""

        if name in cook_book.keys():
            for item in cook_book[name]:

                """ формируем заполнение словаря ингридиентов list_by_dishes в нужном формате, 
                    в случае если такого ингридиента еще не содержится в словаре"""

                if item['ingredient_name'] not in list_by_dishes.keys():

                    list_by_dishes[item['ingredient_name']] = {
                        'measure': item['measure'],
                        'quantity': int(item['quantity']) * person_count
                    }
                else:
                    """ формируем заполнение словаря ингридиентов list_by_dishes в нужном формате, 
                        в случае если такой ингридиент уже содержится в словаре"""

                    # вводим переменную, в которую записываем старое значение количествва необходимых ингридиентов
                    old_quantity = int(list_by_dishes[item['ingredient_name']]['quantity'])

                    list_by_dishes[item['ingredient_name']] = {
                        'measure': item['measure'],
                        'quantity': int(item['quantity']) * person_count + old_quantity
                    }

    return json.dumps(list_by_dishes, ensure_ascii=False, indent=4)


def union_files():
    """
    В папке лежит некоторое количество файлов. Считайте, что их количество и имена вам заранее известны.

    Необходимо объединить их в один по следующим правилам:

    Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них
    (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
    Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем
    Пример
        Даны файлы:
        1.txt

        Строка номер 1 файла номер 1
        Строка номер 2 файла номер 1
        2.txt

        Строка номер 1 файла номер 2

        Итоговый файл:

        2.txt
        1
        Строка номер 1 файла номер 2
        1.txt
        2
        Строка номер 1 файла номер 1
        Строка номер 2 файла номер 1
    """

    # формирование пути к файлу
    current = os.getcwd()
    folder = 'task_3'
    file_name_1 = '1.txt'
    file_name_2 = '2.txt'
    file_name_3 = '3.txt'
    file_name_result = 'result.txt'
    path_full_1 = os.path.join(current, folder, file_name_1)
    path_full_2 = os.path.join(current, folder, file_name_2)
    path_full_3 = os.path.join(current, folder, file_name_3)

    # создание словаря для сохранения информации о количестве строк для каждого файла
    sorted_list = {}

    """ поиск количества строк в каждом файле и добавление информации в словарь, где название файла - ключ, 
        а количество строк в нем - значение"""

    with open(path_full_1, encoding='utf-8') as f:
        sorted_list['1.txt'] = len(f.readlines())

    with open(path_full_2, encoding='utf-8') as f:
        sorted_list['2.txt'] = len(f.readlines())

    with open(path_full_3, encoding='utf-8') as f:
        sorted_list['3.txt'] = len(f.readlines())

    # сортировка данных в словаре по значению
    sorted_list = dict(sorted(sorted_list.items(), key=lambda item: item[1]))

    # формирование цикла по отсортированному словарю для записи данных в файл
    for key in sorted_list:
        # сохранение в переменную информации о количестве строк в файле
        count = sorted_list[key]

        # считывание информации из файла (ключ словаря)
        with open(os.path.join(current, folder, key), encoding='utf-8') as f:
            res = f.readlines()

        # запись информации в файл result.txt в соответствующем заданию формате
        with open(os.path.join(current, folder, file_name_result), 'a+', encoding='utf-8') as file:
            file.writelines([key, "\n", str(count), "\n"])
            file.writelines(res)
            file.write("\n")

    return f"Файлы {file_name_1}, {file_name_2} и {file_name_3} объединены в файл {file_name_result}"
