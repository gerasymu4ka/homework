# -*- coding: utf-8 -*-
#Factorial
#factorial(x)
#factorial(3) → 6
#factorial(4) → 24
#factorial(5) → 120
#factorial for 100-500 should return result in sane time

def factorial(x):
    if x == 0:
        print('Factorial of 0 is 1')
    elif x < 0:
        print("Factorial doesn't exist")
    else:
        for i in xrange(1, x):
            x *= i
        print(x)
    return 

        
