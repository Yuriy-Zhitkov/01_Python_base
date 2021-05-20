'''
Создать (не программно) текстовый файл со следующим содержимым:

One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''


num_dict = {'One': 'Oдин', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('test_task_04.txt', 'r') as obj_from, open('new_task_04.txt', 'w') as obj_to:

    for line in obj_from: # прохожу по каждой строке файла
        a = line.split(' — ') # разделяю строку на два элемента
        if a[0] in num_dict: # делаю замену английского слова на русское, если оно есть в словаре
            a[0] = num_dict[a[0]]
            obj_to.write(' — '.join(a)) # записываю новую строку в выходной файл
        else:
            continue