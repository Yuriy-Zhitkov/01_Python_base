'''
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''


with open('test_task_02.txt', 'r') as obj:

    data = obj.readlines()
    print(f'В файле {obj.name} содержится {len(data)} строк')

    for itm in enumerate(data):
        print(f'Строка №{itm[0]+1} содержит {len(itm[1].split(" "))} слова')
