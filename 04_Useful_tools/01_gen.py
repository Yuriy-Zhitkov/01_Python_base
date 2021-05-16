


# создание генератора
my_list = [2, 4, 6]
new_list = [el+10 for el in my_list] # генератор не изменяет исходный список!!!!
new_list_t = [el+10 for el in my_list]
print(f"Исходный список: {my_list}")
print(f"Новый список 1: {new_list}")

# аналог в виде цикла
new_list_02= []
for el in my_list:
    new_list_02.append(el + 10)
print(f"Новый список 2: {new_list_02}")

# перебор строк файла с помощью генератора
my_lines = [line.strip('\n') for line in open('/Users/Yuriy_IT/Documents/Сравнение Loco 00.16a и 17b/multi.mvc', encoding='cp1251')]
print(my_lines)
for el in my_lines:
    print(el)


# составление словаря с помощью генератора
my_dict_1 = {el: el for el in range(10)}
print(my_dict_1)


# составление словаря с помощью генератора
path = '/Users/Yuriy_IT/Documents/Сравнение Loco 00.16a и 17b/multi.mvc'
my_dict = {el.removesuffix('\n'): [] for el in open(path, encoding='cp1251') if 'with family;' in el}

for val in my_dict.items():
    print(val)



