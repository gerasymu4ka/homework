
#Pythagorean triplets
#x2+y2=z2
#>>> triplets(4)
#[3, 4, 5]
#[6, 8, 10]
#[5, 12, 13]
#[9, 12, 15]

def triplets(x):
    for i in range(1, x + 1):
       # a, b, c = 1, 2, 3
        aside, bside, cside = [], [], []
        for j in range(2, 1000):
            if j % 2 == 0:
                a = j
                b = ((a / 2) ** 2) -1
                c = b + 2
            elif a ** 2 + b ** 2 == c ** 2:
                aside.append(a)
                bside.append(b)
                cside.append(c)
        sides = zip(aside, bside, cside)
        print(list(sides[i]))
      
    return

