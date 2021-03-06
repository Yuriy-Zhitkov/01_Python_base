
# режимы работы с файлами см. документацию!

# для быстрой справки http://pythonicway.com/python-fileio
# r - Открывает файл только для чтения. Указатель стоит в начале файла. (режим по умолчанию)
# rb - Открывает файл для чтения в двоичном формате. Указатель стоит в начале файла.
# r+ - Открывает файл для чтения и записи. Указатель стоит в начале файла.
# rb+ - Открывает файл для чтения и записи в двоичном формате. Указатель стоит в начале файла.
# w - Открывает файл только для записи. Указатель стоит в начале файла. Создает файл с именем имя_файла, если такового не существует.
# wb - Открывает файл для записи в двоичном формате. Указатель стоит в начале файла. Создает файл с именем имя_файла, если такового не существует.
# w+ - Открывает файл для чтения и записи. Указатель стоит в начале файла. Создает файл с именем имя_файла, если такового не существует.
# wb+ - Открывает файл для чтения и записи в двоичном формате. Указатель стоит в начале файла. Создает файл с именем имя_файла, если такового не существует.
# a -
# ab -
# a+ -
# ab+ -

# x - создать и открыть файл на запись. Если файл уже есть, то он не будет создан.
# t -Открыть файл в текстовом формате (режим по умолчанию)

# для указания пути к файлу нужно использовать префикс r'' - это позволит не учитывать \n, \t и т.д
my_file = open(r'/Users/Yuriy_IT/Documents/Сравнение Loco 00.16a и 17b/multi.mvc', 'r')


# режим r
f_1 = open('data.txt', 'r') # режим чтения файла
data = f_1.read() # читает файл целиком. Можно вывести символы с помощью указания идекса
# data = f_1.read(5) # можно указать количество читаемых байт информации
print(data)
print(data[0])
f_1.close()
print('-'*100)


f_1 = open('data.txt', 'r')
print(f_1.readline()) # извлекает и выводит данные файла построчно
print(f_1.readline())
print(f_1.readline())
f_1.close()
print('-'*100)


f_1 = open('data.txt', 'r')
data = f_1.readlines() # извлечь и вывести полный список, состоящий из строк файла
print(data)
print(data[1])
f_1.close()
print('-'*100)


f_3 = open("data.txt", "r")
for line in f_3: # читаем каждую строку в файле
    print(type(line)) # такой способ возвращает тип str
    print(line) # учитываются специальные символы с экранированием: \n, \t и т.д
f_3.close()
print('-'*100)


# цикл, в котором содержимое файла извлекается не более килобайта информации или 1024 байтов (символов)
f_4 = open("data.txt", "r")
while True:
    content = f_4.read(1024)
    print(type(content))
    print(content)
    if not content:
        break
f_4.close()


#
#
# f = open('data2.txt', 'w') # режим записи в файл
# f.write('new line')
# f.close()
#
#
# f = open('data2.txt', 'r') # режим чтения в файл
# print(f.read(5)) # чтение строки частями (чанками)
# print(f.read(5)) # чтение строки частями (чанками)
# f.close()
#

