'''
Поработайте с переменными.
Создайте несколько переменных, выведите на экран,
запросите у пользователя несколько чисел и строк, и сохраните в переменные, выведите на экран.
'''


name = input('Введите ваше имя: ')
age = int(input('Введите ваш возраст: '))
print(f'Вас зовут {name}, вам {age} лет(год)')

# Числовые переменные
a = 1 #тип int
b = 2
c = 4
d = 8
e = 3
f = 0.5 # тип float
print(a + b) # Сложение
print(a - b) # Вычитание
print(a - -b) # Вычитание
print(a * b) # Умножение
print(d / c) # Деление
print(round(d / e, 2)) # Деление с округлением
print(d // e) # Целочисленное деление
print(-d // e) # Целочисленное деление (ВНИМАНИЕ! Целочисленное деление в Python 3 округляет итоговое значение в меньшую сторону)
print(d % e) # Остаток от деления
print(d ** e) #Возведение в степень
print(c ** f) #Извлечение корня


# Строковые переменные
city_1 = 'Москва' #тип str
city_2 = 'Санкт-Петербург'
print(city_1, city_2)


# Списокю кортеж, словарь
list_1 = [a, b, c] # создание списка
print(list_1)
tuple_1 = (a, b, c) # создание кортежа
print(tuple_1)
dict_1 = {'Город' : city_1, 'Столица' : True, "Население" : 12 * 10 ** 6} # создание словаря
dict_2 = {'Город' : city_2, 'Столица' : False, "Население" : 6 * 10 ** 6} # создание словаря
print(dict_1)
print(dict_2)