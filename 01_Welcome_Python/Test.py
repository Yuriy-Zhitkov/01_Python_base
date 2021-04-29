import timeit
code_to_test = """


n = 1111111111

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

"""

elapsed_time = timeit.timeit(code_to_test, number=10000)/10000 * 10**8
print(elapsed_time)
