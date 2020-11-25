
def rotate_letter(letter,num):
	return (ord(letter) + num)

def rotate_word(word,num):
	num_list = []
	for letter in word:
		number_letter = chr(rotate_letter(letter,num))
		num_list.append(number_letter)
	concat_list = "".join(num_list)
	print(concat_list)

rotate_word('house',2)


