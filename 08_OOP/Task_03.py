'''
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.

Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
'''

class ErrorIntList(Exception):

    def __init__(self, text):
        self.text = text


class MyList:

    def input_list(self):
        '''
        Ввод значений и проверка принадлежности значения к типу "число"
        :return: список чисел
        '''
        result = []
        while True:
            try:
                num = input('Введите число (q для выхода): ')
                if num == 'q':
                    print('Программа завершена')
                    break
                elif num.isdigit() == True:
                    result.append(num)
                else:
                    raise ErrorIntList('Ошибка. Введите число!')
            except Exception as e:
                print(e)
            print(result)
        print(result)


some_list = MyList() # создаю экземпляр класса
some_list.input_list() # проверяю работу метода
