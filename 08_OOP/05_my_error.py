import random

# создать исключение (обычно помещаются в отдельный файл)
# существует иерархия ошибок
class Crash(Exception): # ссылаемся на базовый класс Exception
    def __init__(self, txt):
        self.txt = txt



class Auto:

    def __init__(self, brand):
        self.brand = brand

    def run(self, speed):
        num = random.randint(0, 100)
        if speed < 40:
            if crash_num < 5:
                raise Crash('Авария') # вызвать исключение

        elif speed < 110:
            if num < 10:
                raise Crash('Авария')

        else:
            if num < 50:
                raise Crash('Авария')

ferrari = Auto('Ferrary')

try:
    ferrari.run(200)
except Crash: # ловим исключение
    print('Ремонт')
