# It was first variant without storing all multipliers
'''
def max_prime_fact(number):
	if number == 1:
		return number
		
	divider = 2
	current_divider = divider
	
	while number >= divider ** 2:
		if number % divider == 0:
			number //= divider
		else:
			divider += 1
		current_divider = divider
		
	if number > 1:
		current_divider = number
		
	return current_divider
'''	
	
def prime_fact(number):
	if number == 1:
		return number
		
	divider = 2
	primes_mult = []
	
	while number >= divider ** 2:
		if number % divider == 0:
			primes_mult.append(divider)
			number //= divider
		else:
			divider += 1

	if number > 1:
		primes_mult.append(number)
		
	return primes_mult
	
	
test_num = input("Input number to find it's prime multipliers:")	
print "Max prime multiplier is",max(prime_fact(test_num))