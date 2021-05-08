
# 1 Типы данных Python
print('Типы данных Python')
a = 1
b = 'b'
c = [1,2,3]
d = ('a', 'b')

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(d[0]))
print('-' * 100)


# 2 Системы счисления в Python
print('Системы счисления в Python')
print(int(17.7)) # преобразовать к целому числу в десятичном формате (по умолчанию)
print(int('10010', 2)) # преобразовать к целому числу в десятичном формате из другой системы счисления с помощью
                       # дополнительного параметра (от 2 до 36)
print(bin(18)) # преобразовать к двоичному формату
print(oct(18)) # преобразовать к восьмеричному формату
print(hex(18)) # преобразовать к шестнадцатеричному формату
print('-' * 100)


# 3 Операции с целыми числами
print('Операции с целыми числами')
print(abs(-6)) # модуль числа

print(2 << 1) # число 2 в двоичной системе 10 при побитовом двиге влево на 1 позицию превращает в двоичое 100, т.е. число 4
print(int('100', 2)) # проверяем, что двоичное 100 является 4 в десятичной системе

print(2 * 2**3) # арифметическая операция 2*(2^3) (см. https://coderoad.ru/6385792/Что-делает-побитовый-сдвиг-влево-или-вправо-и-для-чего-он-используется)
print(2 << 3) # арифметическая операция 2*2^3 записанная в виде побитового смещения влево

print(16 / 2**3) # арифметическая операция 16/(2^3)
print(16 >> 3) # арифметическая операция 16/(2^3) записанная в виде побитового смещения вправо

print(4 & 6) # побитовое И
print(4 | 6) # побитовое ИЛИ
print(4 ^ 6) # побитовое исключающее ИЛИ
print('-' * 100)


# 4 Комплексные числа
print('Комплексные числа')
comp = complex(5, 6)
print(comp)
print('-' * 100)


# 5 Строки
print('Строки')
s1 = 'abra'
s2 = 'kadabra-123'
w1 = s1 + s2 # конкатинация
print(w1)
w2 = w1[1] # взятие элемента по индексу
print(w2)
# срез - синтаксис: [s:f:step], где s — начало среза, f — окончание, step — шаг (опционально)
print(w1[:3])
print(w1[1:-4])
print(w1[1:10:2])

# реверс строк
print(w1[::-1]) # реверс с использованием среза
# print(reversed(w1)) # такой вариант возвращает сообщение типа <reversed object at 0x10c55ee50>. Почему?????
# реверс на месте
string = "123456789"
str_reverse = ''
symbols = list(string)
for el in range(len(string) // 2):
    tmp = symbols[el]
    symbols[el] = symbols[len(string) - el - 1]
    symbols[len(string) - el - 1] = tmp
    str_reverse = ''.join(symbols)
print(str_reverse)


for el in reversed("abc"): # обратная итерация
    print(el)
print('-' * 100)


# 6 Методы строк
print('Методы строк')
i = 'qwerty, ytrewq'
print(i.split(', ')) # список - деление строки через разделитель
print('ехал гРЕКА через_рЕКУ, видит-грека,в>речке@м'.title()) # строка - Перевести первую букву каждого слова в верхний регистр, остальные - в нижний

print(len(i)) # число - длина строки
print('_'.join(['one', 'two'])) # строка - объединение списка строк через разделитель

a = 1.1

