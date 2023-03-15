import random
n = random.random()
print(n)


import random
n = random.randint(0,100)
print(n)


#Practice using random.sample() method 
import random
#Generate 5 random numbers between 0 and 100
randomlist = random.sample(range(0, 100), 5)
print(randomlist)

# Use For Loop for generating a list of numbers
randomlist = []
for i in range(0,5): 
	n = random.randint(0,100)
	randomlist.append(n)
print(randomlist)
