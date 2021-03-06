'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов.
'''

# решение №1
def my_fync(x, y, z):
    if x == y == z:         # 1 для случая, когда все аргументы имеют одинаковое значение
        return x + y
    else:                   # 2 для остальных случаев
        nums = [x, y, z]                # 2.1 объединение агрументов в список
        ind_min = nums.index(min(nums)) # 2.2 определение индекса аргумента с минимальным значением
        nums.pop(ind_min)               # 2.3 удаление аргумента с минимальным значением
        return sum(nums)                # 2.4 возвращение суммы двух наибольших аргументов
f = my_fync(5, 3, 1)
print(f)


# решение №2
def my_fync_2(x, y, z):
        nums = [x, y, z]                # 1 объединение агрументов в список
        nums.sort(reverse=True)         # 2 сортировка в обратном порядке
        return nums[0] + nums[1]        # 3 возвращение суммы двух наибольших аргументов
f2 = my_fync_2(5, 3, 1)
print(f2)


# решение №3 - через лямбда-функцию
f3 = lambda x, y, z: (sum(sorted([x, y, z], reverse=True)[0:2]), x + y)[x == y == z]
print(f3(5, 3, 1))

