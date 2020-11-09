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




'''
ex06_03
Palindrome: spelled same backward and fordward like "noon"

'''
#the first version of the func doesn't take middle parameters.
def palindrome(word):
	def first(word):
		return word[0]

	def last(word):
		return word[-1]

	def middle(word):
		return word[1:-1]

	if first(word) == last(word) :
		print('{} is a palindrome'.format(word))
	else:
		print('{} is not '.format(word))


#this is a correct function for checking a palindrome
def palindrome_2(word):
	if word[::-1] == word:
		print('{} is a palindrome'.format(word))
	else:
		print('{} is not a palindrome '.format(word))


palindrome_2('moon')
