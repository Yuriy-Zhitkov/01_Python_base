'''
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.

Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * плотность * число см толщины полотна. Проверить работу метода.

'''


class Road:

    def __init__(self, density, length, width, thickness):
        self.density = density # плотность асфальта, кг/м3
        self.length = length # длина участка дороги, м
        self.width = width # ширина участка дороги, м
        self.thickness = thickness # толщина дорожного полотна, см

    def mass(self):
        '''
        Метод определения массы дорожного полотна
        :return: масса, тонны
        '''
        return (self.length * self.width * self.thickness / 100 * self.density) / 1000

road_section_01 = Road(1300, 5000, 20, 5)
mass_of_road = road_section_01.mass()
print(mass_of_road)

