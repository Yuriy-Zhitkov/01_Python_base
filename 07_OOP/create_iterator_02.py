
class Iterator:

    def __init__(self, stop, start=0):
        self.i = start - 1
        self.stop = stop

    def __next__(self):
        self.i += 1
        if self.i <= self.stop:
            return self.i
        else:
            raise StopIteration

    def __iter__(self): # метод возвращает объект у которого есть метод __next__, т.е. сам себя
        return self




a = Iterator(5, 0)
for i in a:
    print(i)


# a = Iterator(5, 0) # создаем ибъект итератор
# while True:
#     try:
#         i = next(a) # вызываем через next объект итератор
#         print(i)
#     except StopIteration:
#         break
