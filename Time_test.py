import time

start_time = time.time()

total = 0
for i in range(1, 1000):
    for j in range(1, 1000):
        total += i + j

print(f'Результат {total}')

end_time = time.time()

print(f'Время выполнения расчета {end_time - start_time : .2f}')