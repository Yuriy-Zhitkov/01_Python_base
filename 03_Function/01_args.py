def my_function(*args):
    for i in args:
        print(i)

my_function(1, 2, 3) # если переменные перечисляются по порядку как аргументы


a = (3, 2, 1)
my_function(*a) # если на вход в качестве аргумента поступает переменная с кортежем


b = [1, 2, 3]
my_function(*b) # если на вход в качестве аргумента поступает переменная со списком