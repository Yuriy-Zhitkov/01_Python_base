import functools as ft

# 1
def my_func(el, next_el):
    '''
    :param el: текущий элемент
    :param next_el: следующий элемент
    :return: элемент
    '''
    return el + next_el

a = ft.reduce(my_func, [1,2,3]) # применяет функцию поледовательно к каждому элементу
print(a)
b = ft.reduce(my_func, ['a','b','c'])
print(b)

# 2
def my_func_2(param1, param2):
    print(param1, param2)
my_func_2('s', 'd')

new_my_func_2 = ft.partial(my_func_2, 'a') # делаем новую функцию и присваиваем 'a' для первого параметра по умолчанию
new_my_func_2('d') # далее новая функция не требует ввод первого параметра

