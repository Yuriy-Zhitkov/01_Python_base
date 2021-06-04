'''
Реализовать базовый класс Worker (работник).
- определить атрибуты: name, surname, position (должность), income (доход);
- последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}

Cоздать класс Position (должность) на базе класса Worker;
- в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
- проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''




class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name # имя
        self.surname = surname # фамилия
        self.position = position # должность
        self._income = {'wage': wage, 'bonus': bonus} # доход



class Position(Worker):

    def get_full_name(self): # полное имя сотрудника
        return f'{self.name} {self.surname}'

    def get_total_income(self): # сумма зарплаты и премии
        return self._income['wage'] + self._income['bonus']




max = Position('Max', 'Jason', 'Head of department', 7000, 2000) # создаю экземпляр класса
print(max.__dict__) # проверяю значения атрибутов

full_name_max = max.get_full_name() # применяю метод для вывода полного имени работника
print(full_name_max)

salary_max = max.get_total_income() # применяю метод расчета суммарного дохода
print(salary_max)

