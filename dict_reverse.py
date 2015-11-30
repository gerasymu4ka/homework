d1 = {1: 11, 2: 22, 3: 33}

d = []
for k, v in d1.items():
    i = (v, k)
    d.append(i)
d2 = dict(d)
print(d2)


#result {33: 3, 11: 1, 22: 2}
