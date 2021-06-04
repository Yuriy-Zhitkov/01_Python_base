
'''
@staticmethod можно использовать для расширения диапазона имен
'''

class User:

    # def __init__(self, name):
    #     self.name = name


    @staticmethod
    def print_info():
        print('Это класс User')


User.print_info() # работает всегда

a = User()
a.print_info() # работает только если указан декоратор @staticmethod