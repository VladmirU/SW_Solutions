def sort_by_length(string):
	
	list_words = string.split()
	list_words = sorted(list_words, key=len)
	return ' '.join(list_words)

original_string = raw_input("Please, input strink to sort it:\n")	
print "Sorted string:\n",sort_by_length(original_string)