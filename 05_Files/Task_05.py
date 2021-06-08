'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

import random

# запись в файл случйных чисел
with open('test_task_05.txt', 'w') as my_file:

    # ввод информации и генерации случайных чисел для записи
    n = int(input('Введите кол-во цифр, которые необходимо сгененрировать: '))
    min = int(input('Укажите нижний предел случайных чисел: '))
    max = int(input('Укажите верхний предел случайных чисел: '))

    # генерация случайных чисел и запись в файл
    random_num = [str(random.randint(min, max)) + ' ' for i in range(n)]
    random_num = ''.join(random_num).removesuffix(' ')
    print(f'Сгенерированы числа: {random_num}, числа записаны в файл {my_file.name}')
    my_file.write(random_num)


# суммирование чисел, записанных  в файле, и вывод значения на экран
with open('test_task_05.txt', 'r') as my_file:
    num = my_file.read().split(' ')
    num = list(map(int, num))
    print(f'Сумма чисел равна {sum(num)}')



