import random

a = random.randint(0, 5) # случайное счисло в указыннх граница, включая границы
print(a)

b = random.randrange(0, 5, 1) # случайное число послендовательности, верхняя граница не включена, нижняя включена
print(b)

c = random.random() # случайное дробное число от 0 до 1, верхняя граница не включена, нижняя включена
print(c * 10) # через умножение можно изменить верхний диапазон
print(c * (10 - 4) + 4) # устанавливаем верхнюю границу 10 и нижнюю границу 4