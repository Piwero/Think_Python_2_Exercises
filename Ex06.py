'''
ex06_02
The Ackermann func
'''

def ack(m,n):
	if m == 0:
		return n+1
		
	elif m >= 0 and n == 0:
		return ack(m-1,1)

	else:
		return ack(m-1,ack(m,n-1))



print(ack(3,4))

print(ack(8,4))
#this one exceed

