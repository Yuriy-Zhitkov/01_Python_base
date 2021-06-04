
class Iterator:

    def __init__(self, stop, start=0):
        self.i = start
        self.stop = stop

    def __next__(self):
        self.i += 1
        if self.i <= self.stop:
            return self.i
        else:
            raise StopIteration


class IterObj: # обычно метод __iter__ и __next__ размещают в одном классе

    def __init__(self, stopp, startt):
        self.startt = startt - 1
        self.stopp = stopp

    def __iter__(self): # метод возвращает объект у которого есть метод __next__
        return Iterator(self.stopp, self.startt)


a = IterObj(5, 0)
for i in a:
    print(i)