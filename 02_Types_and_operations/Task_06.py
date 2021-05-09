'''
* Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь
с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.

Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
'''


# 1 Ввод данных

# 1.1 Формирование списка товаров
things = []
things_num = 1
while True:
    my_exit = input('\nДля выхода введите q, чтобы продолжить нажмите Enter: ')
    if my_exit == 'q':
        break
    print(f'Введите информацию о товаре № {things_num}')
    name = input('Наименование: ')
    prise = input('Стоимость: ')
    quantity = input('Количество: ')
    measure = input('Единица измерения: ')
    things.append((things_num, dict(name=name, prise=prise, quantity=quantity, measure=measure)))
    things_num += 1

# 1.2 вывод списка товаров
print('\nСписок товаров:')
for i in range(len(things)):
    print(things[i])


# 2 Формирование данных для дальнейшей аналитики

# 2.1 подготовка структуры таблицы №1 для заполнения
table_01 = {}
for keys in things[0][1]:
    table_01[keys] = []

# 2.2 заполнение таблицы №1
for i in range(len(things)):
    for itm in things[i][1].items():
        table_01[itm[0]].append(things[i][1][itm[0]])

# 2.3 вывод таблицы №1
print('\nТаблица №1 - Сводная информация о товарах по основным параметрам')
for itm in table_01.items():
    print(itm)