

# пример вызова итераци в генераторе
my_generator = (param * param for param in range(5)) # генератор

# последовательный вызов всех элементов
# for el in my_generator:
#     print(el)

print(next(my_generator)) # вызов следующей итерации в генераторе
print(type(my_generator)) # какой-то код
print(next(my_generator)) # вызов следующей итерации в генераторе

print('-'*100)

def my_generator_2():
    for el in range(10):
        yield el

g = my_generator_2() # присваиваем генератор переменной и спользуем в любой момент в программе
g_2 = my_generator_2()
print(type(g))
print(type(my_generator_2()))

print(next(g), 'первый генератор')
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print(next(g_2), 'другой генератор')
print(next(g_2))

print(next(g), 'опять первый генератор')




