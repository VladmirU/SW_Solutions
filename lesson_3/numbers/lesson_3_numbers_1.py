import math
def is_prime_num(n):
	for div_num in [2, math.sqrt(n)]:
		if n % div_num == 0:
			return False

	return True

n = input()
print is_prime_num(n)