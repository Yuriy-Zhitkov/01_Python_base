'''
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и
рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
'''

class Clothes:

    summary_rate = 0 # общее количество используеммой ткани

    def __init__(self, id, v, h):
        self.id = id # номер заказа
        self.v = v # ширина см
        self.h = h # рост, см

    @property
    def thread_length(self): # подстчет длины нити
        return 2 * (self.v + self.h)


class Coat(Clothes):

    def rate(self):
        rate = self.v / 6.5 + 0.5 # расчет расхода ткани
        Clothes.summary_rate += rate
        return rate

    @property
    def cost(self):
        return self.rate() * 100

class Suit(Clothes):

   def rate(self):
        rate = 2 * self.h + 0.3 # расчет расхода ткани
        Clothes.summary_rate += rate
        return rate

   @property
   def cost(self):
       return self.rate() * 130

class Trousers(Clothes):

    def rate(self):
        rate = self.v / 3.5 + 0.25 # расчет расхода ткани
        Clothes.summary_rate += rate
        return rate

    @property
    def cost(self):
        return self.rate() * 80


my_coat = Coat(112, 48, 190)
my_suit = Suit(113, 52, 176)
my_trousers = Trousers(114, 46, 178)


print(f'Для заказа №{my_coat.id} необходимо {my_coat.rate()} метров ткани и {my_suit.thread_length} метров нити\n'
      f'Себестоимость заказа {round(my_coat.cost, 2)} рублей\n')
print(f'Для заказа №{my_suit.id} необходимо {my_suit.rate()} метров ткани {my_suit.thread_length} метров нити\n'
      f'Себестоимость заказа {round(my_suit.cost, 2)} рублей\n')
print(f'Для заказа №{my_trousers.id} необходимо {my_trousers.rate()} метров ткани {my_trousers.thread_length} метров нити\n'
      f'Себестоимость заказа {round(my_trousers.cost, 2)} рублей\n')

print(f'Общее количество используеммой ткани {round(Clothes.summary_rate, 2)} метров')
