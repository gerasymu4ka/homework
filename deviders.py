
#First 100 divisible by 3, 5, but not both
#3 5 9 10 12 18 20 ...

def deviders(n, n1):
	# n = int(raw_input('Enter first number in range: '))
	# n1 = int(raw_input('Enter last number in range: '))
	if n > n1 or n == n1:
	    return ('Last number in range have to be bigger than first')
	else:
    
		count = 0
		lst = []
		for i in range(n, n1):
		   if i % 3 == 0 or  i % 5 ==0:
		       lst.append(i)
		   
		   count += 1
		   if count == 100:
		       break
		# print lst
		# print('''
		# OR
		# ''')
		# count = 0
		# lst = [i for i in range(n, n1) if i % 3 == 0 or  i % 5 ==0] #count?

		return lst



    
