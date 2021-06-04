'''
 Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
 передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
 а также других данных, можно использовать любую подходящую структуру, например словарь.
'''


class Storage:

    display_list = []
    key_board_list = []
    mouse_list = []

    def __init__(self, cells):
        self.cells = cells


    @staticmethod
    def cell_busy(*args): # метод подсчета занятых ячеек
        return sum([len(el) for el in args])


    def info(self):
        print(f'Склад всего содержит {self.cells} ячеек')
        print(f'Занято ячеек ')



class Thing:


    def __init__(self, prise: int, weight: int, size: str, nums: int):
        self.nums = nums
        self.size = size
        self.weight = weight
        self.prise = prise


    def __str__(self):
        return f'{self.__dict__}'


    def move(self):
        self.__dict__['place'] = input('Введите место, где находится предмет: ')


class Display(Thing):

    def __init__(self, diagonal: int, prise: int, weight: int, size: str, nums: int):
        super().__init__(prise, weight, size, nums)
        self.diagonal = diagonal

    @classmethod
    def new(cls):
        print('Введите информацию о мониторе: diagonal: дюймы, prise: рубли, weight: кг, size: д-ш-в, nums: шт')
        description_thing = [input() for _ in range(5)]
        return Storage.display_list.append(cls(*description_thing))




class KeyBoard(Thing):

    def __init__(self, type_k: str ,prise: int, weight: int, size: str, nums: int):
        super().__init__(prise, weight, size, nums)
        self.type_k = type_k


    @classmethod
    def new(cls):
        print('Введите информацию о клавиатуре: type_k: тип, prise: руб, weight: кг, size: д-ш-в, nums: шт')
        description_thing = [input() for _ in range(5)]
        return Storage.key_board_list.append(cls(*description_thing))



class Mouse(Thing):

    def __init__(self, type_m: str, prise: int, weight: int, size: str, nums: int):
        super().__init__(prise, weight, size, nums)
        self.type_m = type_m

    @classmethod
    def new(cls):
        print('Введите информацию о мышке: type_m: тип, prise: руб, weight: кг, size: д-ш-в, nums: шт')
        description_thing = [input() for _ in range(5)]
        return Storage.mouse_list.append(cls(*description_thing))






# Добавление новых товаров
a = Display.new()
b = KeyBoard.new()
c = Mouse.new()

# Вывод на экран (для проверки)
print(Storage.display_list[0])
print(Storage.key_board_list[0])
print(Storage.mouse_list[0])

# Перемещение товара на новое место
Storage.display_list[0].move()
print(Storage.display_list[0])