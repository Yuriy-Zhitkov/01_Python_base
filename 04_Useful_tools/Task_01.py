'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

# функция расчета заработной платы
def slr(hr = 0, pay = 0, pr = 0):
    '''
    :param hr: часы
    :param pay: оплата в час
    :param pr: премия
    :return: зарплата за указанное количество часов
    '''
    return (hr * pay) + pr

# информация о работе
Tom_work = {'jun': {'hours': 168, 'payment': 3000, 'premium': 20000},
            'feb': {'hours': 150, 'payment': 3000, 'premium': 10000},
            'march': {'hours': 168, 'payment': 3000, 'premium': 20000}
            }

# вариант №1
# расчет заработной платы на каждый месяц
Tom_salary = []
for key in Tom_work:
    Tom_salary.append(slr(Tom_work[key]['hours'], Tom_work[key]['payment'], Tom_work[key]['premium']))
print(Tom_salary)


# вариант №2
Tom_salary_2 = [slr(Tom_work[key]['hours'], Tom_work[key]['payment'], Tom_work[key]['premium']) for key in Tom_work]
print(Tom_salary_2)




