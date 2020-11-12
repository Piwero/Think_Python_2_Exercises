import math

def check_fermat(a, b, c, n):
	if n > 2 and a**n + b**n == c**n:
		print ("Fermat is wrong!")
	else:
		print ("Fermat is right on this!")
		

def run_cf():
	for a in range(1, 100):
		for b in range(1, 100):
			for c in range(1, 100):
				for n in range(3, 100):
					check_fermat(a, b, c, n)
      
          

def check_fermat_custom():
	a = int(input("Please in put a: "))
	b= int(input("Please in put b: "))
	c = int(input("Please in put c: "))
	n = int(input("Please input n: "))
	return check_fermat(a, b, c, n)
  
  
  check_fermat_custom()

#this command works very well
# I'm trying this from git