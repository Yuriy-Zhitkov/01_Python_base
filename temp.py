import itertools as it

# my_list = [print(i) for i in range(100) if i <= 10]
my_list = [print(i) for i in it.count(100) if i <= 10]


