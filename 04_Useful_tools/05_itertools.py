import itertools as it


# обычный перебор элементов
for el in range(7,11):
    print(el)

print('-'*100)

# перебор с итераторм
for el in it.count(7): # итераци идут от 7 до указанного условаия выхода
    if el > 10:
        break
    else:
        print(el)

print('-'*100)

# перебор элементов
i = 0
for el in it.cycle('ABC'):
    print(el)
    i += 1
    if i == 9: break

print('-'*100)

# вызов cycle с помощью next
def my_func():
    for el in it.cycle('ABC'):
        yield el

iter = my_func()
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

print('-'*100)

progr_lang = ["python", "java", "perl", "javascript"]
iter_2 = it.cycle(progr_lang)
print(next(iter_2))
print(next(iter_2))
print(next(iter_2))
print(next(iter_2))
print(next(iter_2))
print(next(iter_2))


# повторение объекта
for el in it.repeat('Hello', 3):
    print(el)

my_repeat = list(it.repeat('hi', 3))
print(my_repeat)


# комбинации (можно выполнить и в цикле)
my_combination = list(it.combinations([1, 2, 3], 2))
print(my_combination)

print('-'*100)

# разные итераторы
print(list(it.product('ABCD', 'ABCD'))) #--> AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD # полное перемножение с дублями
print(list(it.permutations('ABCD',2))) #--> AB AC AD BA BC BD CA CB CD DA DB DC # полное перемножение без дублей
print(list(it.combinations_with_replacement('ABCD', 2))) #--> AA AB AC AD BB BC BD CC CD DD # без "зеркальных пар" с дублями
print(list(it.combinations('ABCD', 2))) #--> AB AC AD BC BD CD # без "зеркальных пар" без дублей

