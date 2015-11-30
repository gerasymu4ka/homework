
#First 100 divisible by 3, 5, but not both
#3 5 9 10 12 18 20 ...

n = int(raw_input('Enter first number in range: '))
n1 = int(raw_input('Enter last number in range: '))
if n > n1 or n == n1:
    print('Last number in range have to be bigger than first')
    
count = 0
for i in range(n, n1):
    if i % 3 == 0 or  i % 5 ==0:
        print(i)
    i += 1
    count += 1
    if count == 100:
        break

print('''
OR
''')

i = [i for i in range(n, n1) if i % 3 == 0 or  i % 5 ==0]
print(i)
    
