
import struct


#Чтение бинарных (двоичных) файлов
# файл Test.sgr также есть в папке проекта 04_Useful_tools
my_file = open(r'/Users/Yuriy_IT/Documents/R/Read UM Binnary/Test.sgr', 'rb')


# рабочий способ
data = my_file.read()
my_list = []
for i in range(int(len(data)/4)): # цифра 4 означает, что в 4 битах содержится единица информации
    el = data[i * 4 : i * 4 + 4] # срезаю из файла 4 бита
    el = struct.unpack('f', el) # преобразую бинарный формат в число с плавающей точкой (возвращается кортеж)
    my_list.append(list(el)[0]) # преобразую кортеж el в список и добавляю значение в свой список my_list
print(my_list)


# не работает
# data1 = my_file.read()
# my_list = []
# for i in range(int(len(data1)/4)):
#     data = my_file.readline(4) # отсекаю 4 бита
#     T = struct.unpack('f', data) # преобразую в число с плавающей точкой
#     my_list.append(T) # подсоединяю к списку
# print(my_list)






