'''
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func()
'''


# 1 функция для обработки одного слова
def int_func(chrt):
    symbols = {'a':'A', "b":"B", 'c':'C', 'd':'D', 'e':'E','f':'F', 'g':'G', 'h':'H', 'i':'I', 'j':'J', 'k':'K', 'l':'L',
               'm':'M', 'n':'N', 'o':'O', 'p':'P', 'q':'Q', 'r':'R', 's':'S', 't':'T', 'u':'U', 'v':'V', 'w':'W', 'x':'X',
               'y':'Y', 'z':'Z'}
    chrt_list = list(chrt) # преобразуем строку в список символов
    if chrt_list[0] in symbols: # проверка, что первый символ - это строчная буква
        chrt_list[0] = symbols[chrt_list[0]] # заменяем первую букву на прописной вариант
    else:
        pass
    chrt = ''.join(chrt_list) # преобразуем список символов обратно в строку
    return chrt

print(int_func('asd'))


# 2 функция для обработки нескольких слов
def int_func_02(some_text):
    some_text_list = some_text.split(' ') # разбиваем строку, преобразуя в список
    while '' in some_text_list:  # удаление пустых элементов
        some_text_list.remove('')
    for i in range(len(some_text_list)): # применение функции int_func к каждому слову
        some_text_list[i] = int_func(some_text_list[i])
    chrt = ' '.join(some_text_list) # преобразуем список слов обратно в строку
    return chrt

print(int_func_02('aw  aw. sdds wef ghjg ef '))
print(int_func_02('aw aw 4f kb !s'))
