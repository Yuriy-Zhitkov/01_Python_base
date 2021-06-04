'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''

class Data:

    def __init__(self, datatata: str):
        self.datatata = datatata

    def data(self):
        return list(map(int, self.data_int(self.datatata)))

    @staticmethod
    def data_int(some_data: str):
        return (some_data.split('-'))





my_data = Data('23-05-89')
print(my_data.data())






