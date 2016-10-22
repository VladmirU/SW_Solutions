def pattern(n):
	string = '1'
	for i in range(2, n + 1):
		string += ('\n1' + '*' * (i - 1) + str(i))
		
	return string