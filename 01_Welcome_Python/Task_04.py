'''
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''

n = int(input('Введите целое число: '))

# определяем длину введенного числа
length = 0
nn = n
if nn == 0:
    length = 1
else:
    while nn != 0:
        length += 1
        nn //= 10
print('Длина числа равна', length)

# определяем наибольшую цифру в числе
i = 0
max_number = 0
nn = n
while i <= length:
    number = nn // (10 ** (length - i))
    if number > max_number:
        max_number = number
    nn = nn % (10 ** (length - i))
    i += 1
print(f'Число {n} состоит из {length} цифр, наибольшая цифра {max_number}.')