'''
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
'''

begin = int(input('Введите длину (км) дистанции в первый день тренировки: '))
purpose = int(input('Введите цель тренировки в км: '))

day = 1
result = begin
while result < purpose:
    day += 1
    result *= 1.1
print(f'На {day}-й день спортсмен достиг результата — не менее {purpose} км')