fin = open('words.txt')

'''
V1 for showing list of words without e

def has_no_e(word):
	result = ""
	for letter in word:
		if letter == 'e':
			result = False
			break
		else:
			result = True
	if result == False:
		pass
	else:
		print(word)


for word in fin:
	count(has_no_e(word))

'''

counter = 0
result_list = []

def has_no_e(word):
	global counter
	result = ""
	for letter in word:
		counter+=1
		if letter == 'e':
			result = False
			break
		else:
			result = True
	if result == False:
		pass
	else:
		result_list.append(word)


for word in fin:
	has_no_e(word)

words_no_e = len(result_list)
percentage = round((words_no_e/counter)*100,2)



print("word without e = " + str(words_no_e))
print("total words from file = " + str(counter))
print("the % of words with 'e' in total is = " + str(percentage) +"%")









