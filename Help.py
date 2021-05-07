# Вызов справки
help(int) # вызов справки для класса
help(int.split) #вызов справки для класс.метод
help(random.)


# вывод списка методов для объекта (str, list и т.д)
# https://coderoad.ru/1911281/Как-получить-список-методов-в-классе-Python
print (dir(str))
print (dir(dict))
print('-'*100)

# Получить список аргументов функции
# https://webhamster.ru/mytetrashare/index/mtb339/1551698682fyxh0kqst2
import inspect # подключение модуля
def foo(a,b,c=3, *arglist, **keywords): pass # пример функции
print(inspect.getfullargspec(foo))
# args -- имена позиционных параметров
# varargs -- имя аргумента со звёздочкой * или None
# varkw -- имя аргумента с двемя звездочками ** или None
# defaults -- n-tuple со значениями по умолчанию, соответствуют последним n элементам из args
# kwonlyargs -- имена только именованных аргументов (которые идут после * или **)
# kwonlydefault -- значения по умолчанию для только именованных аргументов
# annotations -- маппинг значений аргументов на аннотации