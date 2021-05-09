'''
Реализовать структуру «Рейтинг», представляющую собой невозрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен
разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
'''

my_list = [6, 4, 2, -2, -4, -6]
my_list.sort(reverse=True)
print(my_list)

while True:
    number = int(input('Введите натуральное число: '))
    if my_list.count(number) > 0:
        ind = my_list.index(number)
        my_list.insert(ind, number)
    else:
        if number >= 0:
            ind = 0
            for i in range(number, max(my_list)+1):
                ind += my_list.count(i)
            my_list.insert(ind, number)
        else:
            ind = 0
            for i in range(number, min(my_list)-1, -1):
                ind += my_list.count(i)
            my_list.insert(len(my_list)-ind, number)

    print(my_list)
