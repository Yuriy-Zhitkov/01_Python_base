
# Случай 1 - обработка ошибки в функции main
# Проблемы:
# не понятно, что за ошибка
# расчет в функции main прерывается, если встречается ошибка

# def div(*args):
#     for i in args:
#         print(10 / i)
#
#
# def main():
#     data = [(10, 20, 0, 100, 140), (55, 47, 98, 45, 34)]
#     for ds in data:
#         try:
#             div(*ds)
#         except:
#             print('Error') # выводим текст при возникновении ошибки
#         print('-'*50)
#
# main()


# Случай 2 - исправляем первую проблему
# def div(*args):
#     for i in args:
#         print(10 / i)
#
#
# def main():
#     data = [(10, 20, 0, 100, 140), (55, 47, 98, 45, 'qwerty')]
#     for ds in data:
#         try:
#             div(*ds)
#         # except:
#         #     print('Error')
#         except Exception as e: # присваиваем значение ошибки Exception в переменную e
#             print('Error', e)
#         print('-'*50)
#
# main()


# Случай 3 - исправляем вторую проблему
# ZeroDivisionError и TypeError обработалось в div, остальное в main
def div(*args):
    for i in args:
        try:
            print(10 / i)
        # except (ZeroDivisionError, TypeError):
        #     print('Ошибка')
        except ZeroDivisionError: # обрабатываем ошибку
            print('Ошибка. Деление на ноль')
        except TypeError: # обрабатываем ошибку
            print('Ошибка. Ожидаемый тип - int')




def main():
    data = [(10, 20, 0, 100, 140), (55, 47, 'qwerty', 45, 3), 23]
    for ds in data:
        try:
            div(*ds)
        except Exception as e: # присваиваем значение ошибки Exception в переменную e
            print('Error', e)
        print('-'*50)

main()

# случай обработки ошибки на самом высоком уровне
try:
    main()
except Exception as e:
    print(e)


# else -> finaly
try:
    res = 100/0
except ZeroDivisionError:
    print("На ноль делить нельзя")
else:
    print(f"Все хорошо. Результат - {res}")
finally:
    print("Программа завершена")
    print("_" * 50)


# модуль traceback для перевода ошибки в строковый формат
# можно использовать, например, для записи логов

import traceback

try:
    res = 100/0
except Exception as e:
    print(traceback.format_exc())
else:
    print(f"Все хорошо. Результат - {res}")
finally:
    print("Программа завершена")