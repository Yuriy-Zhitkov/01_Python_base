'''
Разработаем виртуальную модель образовательного процесса.
Для этого в программе выделим следующие объекты: студенты, преподаватель, знания
'''


class Person: # главный класс Персона

    def __init__(self, name, surname):
        self.name = name # имя
        self.surname = surname # фамилия

    def __str__(self):# переопределяем вывод строки
        return f"Name and surname: {self.name} {self.surname}"


class Teacher(Person): # класс Учитель

    def to_teach(self, subj, *pupils): # метод обучение
        for pupil in pupils: # перебираем каждого Ученика
            pupil.to_take(subj) # присваиваем ученику Предметы, которые преподает Учитель


class Pupill(Person): # класс Ученик

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.knowledges = [] # пустой список в который записывается перечень Предметов

    def to_take(self, subj):
        self.knowledges.append(subj) # записываем под индексом 0 список Предметов


class Subject: # класс Предметы

    def __init__(self, *subjects):
        self.subjects = list(subjects) # преобразуем перечень Предметов в список

    def my_list(self):
        return self.subjects # возвращаем список Предметов



s = Subject("maths", "physics", "chemistry")
t = Teacher("Ivan", "Ivanov")
print(t)
p_1 = Pupill("Petr", "Petrov")
p_2 = Pupill("Sergey", "Sergeev")
p_3 = Pupill("Vladimir", "Vladimirov")
print(f"{p_1}; {p_2}; {p_3}")
# print(p_1.__dict__)
t.to_teach(s, p_1, p_2, p_3)
# print(p_1.__dict__)

# выводим список Предметов на одного студента
print(p_1.knowledges[0].my_list()) # в knowledges[0] содержится экземпляр Subject, для возврата используется метод my_list

