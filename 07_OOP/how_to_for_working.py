data = [1,2,3,'hello']

# 01 цикл for
# for i in data:
#     print(i)

# копия предыдущего цикла
iobj = data.__iter__() # создаем ибъект итератор
while True:
    try:
        i = next(iobj) # вызываем через next объект итератор
        print(i)
    except StopIteration:
        break

