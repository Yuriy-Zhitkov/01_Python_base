num = 11
n = 3

# lines = num // n
# piece = num - num // n * n
# for i in range(lines):
#     print('*' * n)
# print('*' * piece)

c = ''
for i in range(num):
    if i % n != 0 or i == 0:
        c += '*'
    else:
        c += '\n*'

print(c)