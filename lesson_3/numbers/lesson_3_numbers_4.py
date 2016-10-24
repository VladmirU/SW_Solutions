def sum_mult_num(number):
	mult_num = 1
	sum_num = 0
	while number > 0:
		div = number % 10
		mult_num *= div
		sum_num += div
		number //= 10
	
	return sum_num, mult_num
	
test_num = input('Input test number:')
print 'Sum of digits is {0} and multiplication is {1}'.format(*sum_mult_num(test_num))