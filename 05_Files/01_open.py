f = open('data.txt', 'r') # режим чтения файла
# data = f.read() # или
data = f.readlines() # или
print(data)
f.close()


f = open('data2.txt', 'w') # режим записи в файл
f.write('new line')
f.close()


f = open('data2.txt', 'r') # режим чтения в файл
print(f.read(5)) # чтение строки частями (чанками)
print(f.read(5)) # чтение строки частями (чанками)
f.close()


