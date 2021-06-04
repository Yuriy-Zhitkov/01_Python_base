'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
'''

class Complex:

    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __str__(self):
        return (f'{self.r}+{self.i}i', f'{self.r}{self.i}i')[self.i < 0]

    def __add__(self, other):
        return Complex((self.r + other.r), (self.i + other.i))

    def __mul__(self, other):
        return Complex((self.r * other.r - self.i + other.i), (self.i * other.r + self.r + other.i))



a = Complex(2, 3)
b = Complex(-1, 0)
print(a)
print(b)

c = a + b
d = a * b
print(c)
print(d)




