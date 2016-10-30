def pig_latin(string):
	words_list = string.split()
	edited_list = []
	vowels = 'aeiouy'
	count = 1
	for word in words_list:
		if word[0].lower() in vowels:
			edited_list.append(word + 'way')
		else:
			while word[count] not in vowels:
				count += 1
				if count == len(word):
					break
			edited_list.append(word[count::] + word[:count:] + 'ay')
			count = 1
				
	return ' '.join(edited_list)
	

original_string = raw_input('Please, input string:\n')	
print('\nPig latin string is:')
print pig_latin(original_string)