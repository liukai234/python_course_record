import random

list=""

for i in range(4):
	j=random.randrange(0,4)
	
	if j == 1:
		list = list + str(random.randrange(0,10))
	elif j == 2:
		list = list + chr(random.randrange(65,91))
	else:
		list = list + chr(random.randrange(97,123))

print(list)
