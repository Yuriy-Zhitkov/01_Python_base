'''
Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.
'''

def user_info(name = None,
            last_name = None,
            year_of_birth = None,
            city = None,
            email = None,
            phone_num = None):
    '''
    :param name: имя
    :param last_name: фамилия
    :param year_of_birth: год рождения
    :param city: город проживания
    :param email: адрес электронной почты
    :param phone_num: номер телефона
    :return: вывод на экран информации о пользователе
    '''
    print(f'{name} {last_name} родился в {year_of_birth} году, проживает в городе {city}. '
          f'Телефон для связи: {phone_num}. '
          f'E-mail: {email}')

user_info('Анатолий', 'Воронов', 1993, 'Москва', 'a.voron@ya.ru', 89235632)