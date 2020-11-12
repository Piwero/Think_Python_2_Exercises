'''
Ex06_04

func is power

a is a power of b if its divisible by b
and a/b is a power of b.

Take parameters (a,b) returns True if a is a power b


'''


def is_power(a, b):
	if(a == b): #base case a = b
		return True
	elif(a % b != 0):
		return False
	else:
		return is_power(a/b , b)

print(is_power(6,2))
