'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def my_func(x, y):
    '''
    Возвращает частное двух чисел
    :param x: числитель
    :param y: знаменатель
    :return: частное двух чисел. При делении на ноль, возвращается None
    '''
    if x == 0 or y == 0:
        return None
    else:
        return x / y

print(my_func(8, 1))