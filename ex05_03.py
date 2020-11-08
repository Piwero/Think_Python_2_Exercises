
def is_triangle(a,b,c):
	if a > 2*(b +c) or b > 2*(a +c) or c > 2*(b +a):
		print("NO")
	else:
		print("YES")

#test YES
is_triangle(8,2,2)

#test NO
is_triangle(9,2,2)
