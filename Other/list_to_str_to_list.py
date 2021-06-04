
# Превращение списка в строку и обратно

import ast

a = [1,2,3,4,'sd']

b = str(a)
bb = '[1, 2,3,4,5]'

print(b)
print(type(b))

# c = ''.join(b)
c = eval(b)
cc = eval(bb) #https://proglib.io/p/dinamicheskoe-vypolnenie-vyrazheniy-v-python-funkciya-eval-2020-05-14
ccc = ast.literal_eval(bb) # https://digitology.tech/docs/python_3/library/ast.html

print(c)
print(type(c))

print(cc)
print(type(cc))

print(ccc)
print(type(ccc))


