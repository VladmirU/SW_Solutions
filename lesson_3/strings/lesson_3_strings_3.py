def sum_mult_str(number):
	total_sum = 0
	total_mult = 1
	for digit in number:
		digit = int(digit)
		total_sum += digit
		total_mult *= digit
	return (total_sum, total_mult)
	
string = raw_input("Please, input number: ")
print "The sum of the digits is {}\nThe multiplication of the digits is {}".format(*sum_mult_str(string))
