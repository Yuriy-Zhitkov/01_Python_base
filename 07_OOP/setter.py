

class Auto:

    # конструктор класса Auto
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    # создаем свойство года
    @property
    def year(self):
        return self.__year

    # сеттер для создания свойств
    @year.setter
    def year(self, year):
        if year >= 2021:
            self.__year = 2021
        elif year <= 1990:
            self.__year = 1990
        else:
            self.__year = year

    def ge_auto_year(self):
        return f'Автомобиль выпущен в {str(self.year)} году'

a = Auto('df', 2090)
print(a.ge_auto_year())