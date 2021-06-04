'''
@classmethod - используется, когда нужно в качестве первого аргумента передать класс
self - это объект, cls - это класс
'''

class Boss:

    @classmethod
    def create_attr(cls):
        print(cls.__name__)
        cls.attr = '111'

class A(Boss):
    pass

class B(Boss):
    pass


Boss.create_attr()
A.create_attr()
B.create_attr()

print(Boss.__dict__)