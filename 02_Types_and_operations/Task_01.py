'''
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно,
в программе.
'''

my_list = [1,
           1.2,
           complex(1, 7),
           'a',
           True,
           [1, 2, 3],
           (11, 22, 33),
           {'a', 'a', 'b', 'c'},
           {'name': 'Nick', 'age': 25},
           b'Some text',
           None]

for num, el in enumerate(my_list, 1):
    print(f'{num} Элемент со значением {el} относится к -->> {type(el)}')