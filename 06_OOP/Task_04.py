'''
Реализуйте базовый класс Car:
- у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
- опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
- добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
- для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
'''

class Car:

    def __init__(self, speed, color, name, is_polise):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_polise

    def go(self):
        print(f'Автомобиль {self.name} поехал')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        print(f'Автомобиль {self.name} повернул на {direction}')

    def show_speed(self):
        print(f'У водителя {self.name} текущая скорость {self.speed}')


class TownCar(Car):

    max_speed = 60 # можно ли по ходу выполнения программы переназначить этот параметр???

    def __init__(self, speed, color, name, is_polise, invalid):
        Car.__init__(self, speed, color, name, is_polise)
        self.invalid = invalid

    def show_speed(self):
        if self.speed <= TownCar.max_speed:
            print(f'У водителя {self.name} текущая скорость {self.speed}')
        else:
            print(f'У водителя {self.name} превышение скорости!!! Допустимая скорость {TownCar.max_speed}')


class WorkCar(Car):

    max_speed = 40

    def __init__(self, speed, color, name, is_polise, loaded):
        Car.__init__(self, speed, color, name, is_polise)
        self.loaded = loaded

    def show_speed(self):
        if self.speed <= WorkCar.max_speed:
            print(f'У водителя {self.name} текущая скорость {self.speed}')
        else:
            print(f'У водителя {self.name} превышение скорости!!! Допустимая скорость {WorkCar.max_speed}')


class SportCar(Car):

    def __init__(self, speed, color, name, is_polise, brand):
        Car.__init__(self, speed, color, name, is_polise)
        self.brand = brand


class PoliseCar(Car):

    def __init__(self, speed, color, name, is_polise, on_line):
        Car.__init__(self, speed, color, name, is_polise)
        self.on_line = on_line

    def signal(self):
        print(f'Полицейская машина {self.name} включила проблесковые маячки')


max_car = TownCar(40, 'yellow', 'Max', False, False)
kate_car = WorkCar(60, 'yellow', 'Kate', False, False)
jack_car = SportCar(120, 'yellow', 'Jack', False, 'BMW')
tom_car = PoliseCar(40, 'yellow', 'Tom', True, False)

print(max_car.__dict__)
print(kate_car.__dict__)
print(jack_car.__dict__)
print(tom_car.__dict__)

print('-' * 100)

max_car.go(), kate_car.go(), jack_car.go()
max_car.show_speed(), kate_car.show_speed(), jack_car.show_speed()
tom_car.go(), tom_car.signal()
kate_car.turn('Left'), jack_car.turn('Left'), tom_car.turn('Left')
kate_car.stop(), jack_car.stop(), tom_car.stop()




