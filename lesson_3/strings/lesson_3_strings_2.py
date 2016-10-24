def shortest_length(original_string):
	
	list_of_words = original_string.replace(',', ' ').replace('.', ' ').replace(':', ' ').replace(';', ' ').replace('"', ' ').split()
	min_length = len(list_of_words[0])
	for word in list_of_words[1::]:
		if min_length == 1:
			return min_length
		elif len(word) < min_length:
			min_length = len(word)
	return min_length

original_text = raw_input("Please, input string to analize it: ")
print "Length of shortest word is {}".format(shortest_length(original_text))