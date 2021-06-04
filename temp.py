

class MyClass:

    def __init__(self, a, b, c):
        self.c = c
        self.b = b
        self.a = a

    @staticmethod
    def pr():
        res = [1,2,3,4,5]
        return res

    @classmethod
    def in_to(cls):
        print('Введите три значения через запятую:')
        description_thing = tuple([11, 22, 33])
        return cls(*description_thing)

    # @classmethod
    # def in_to(cls):
    #     print('Введите три значения через запятую:')
    #     description_thing = tuple([11, 22, 33])
    #     return Other(*description_thing)


    def out(self):
        return [self.a, self.b, self.c]

class Other(MyClass):

    def a(self):
        pass





aa = MyClass(1,2,5)
aa.pr()
print(aa.out())
#
bb = MyClass.in_to()
print(bb.out())

cc = Other.in_to()
print(cc.out())

