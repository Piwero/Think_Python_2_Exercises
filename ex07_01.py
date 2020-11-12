
import math

def mysqrt(a):
	x =1
	while True:
		y = (x+ a/x) / 2
		if y == x:
			break
		x=y
	return x


def test_square_root():
	a = 1
	print("a"+ " "*14 + "mysqr(a)" + " "*14+ "math.sqrt(a)" + " "*14 + "diff")
	print("-"+ " "*14 + "---------" + " "*14 + "---------" + " "*16 + "----")
	for i in range(1,10):
		mysqrt(a)
		d =  mysqrt(a)- math.sqrt(a)
		print(str(i)+ " "*14+ str(float(mysqrt(i)))+ " "*18+ str((math.sqrt(i)))+ " "*18+ str('{}'.format(d)))
		a+=1
test_square_root()
