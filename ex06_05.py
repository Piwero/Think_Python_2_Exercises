'''
Ex06_05

greatest common divisor = largest number that divides both with no remainder. 

'''
def gcd(a, b):
	a = int(a)
	b = int(b)
	if a > b:
		r = a - b
		gcd(b, r)
	elif a < b:
		r = b - a
		gcd(a, r)
	else:
		print(a)
		
gcd(2523, 1052)
		

