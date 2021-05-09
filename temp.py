a = dict(k= [1,2,3], l= [])

print(a)

for itm in a.items():
    a[itm[0]] = itm[1].append(999)
    print(itm[0])
    print(itm[1])




print(a)

