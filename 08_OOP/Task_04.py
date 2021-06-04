'''
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
'''

class Storage:

    def __init__(self, cells):
        self.cells = cells


    @staticmethod
    def cell_busy(*args): # метод подсчета занятых ячеек
        return sum([el for el in args])



    def info(self):
        print(f'Склад всего содержит {self.cells} ячеек')
        print(f'Занято ячеек ')



class Thing:

    def __init__(self, prise: int, weight: int, size: list, nums: int):
        self.nums = nums
        self.size = size
        self.weight = weight
        self.prise = prise


class Display(Thing):

    def __init__(self, diagonal: int, prise: int, weight: int, size: list, nums: int):
        super().__init__(prise, weight, size, nums)
        self.diagonal = diagonal


class KeyBoard(Thing):

    def __init__(self, type_k: str ,prise: int, weight: int, size: list, nums: int):
        super().__init__(prise, weight, size, nums)
        self.type_k = type_k


class Mouse(Thing):

    def __init__(self, type_m: str, prise: int, weight: int, size: list, nums: int):
        super().__init__(prise, weight, size, nums)
        self.type_m = type_m


storage_01 = Storage(150)
storage_01.info()

mouse_01 = Mouse('оптическая', 1500, 150, [6, 5, 4], 13)
key_board_01 = KeyBoard('оптическая', 2500, 700, [36, 18, 2], 15)
display_01 = Display(37, 2500, 700, [36, 18, 2], 56)


a = storage_01.cell_busy(mouse_01.nums, key_board_01.nums,display_01.nums)
print(a)




