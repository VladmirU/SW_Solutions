def count_percentages(original_string):
	letters_count = 0
	digit_count = 0
	for symbol in original_string:
		if symbol.isalpha():
			letters_count += 1
		if symbol.isdigit():
			digit_count += 1
	letters_percent = (letters_count * 1.0) / len(original_string) * 100
	digit_percent = (digit_count * 1.0) / len(original_string) * 100
	spec_symb_percent = 100.0 - letters_percent - digit_percent
	return {'Letters':letters_percent, 'Digits':digit_percent, 'Spec_symbols':spec_symb_percent}
			
test_text = raw_input("Please, input string to analize:")

result = count_percentages(test_text)

print "Percent of letters is: {letters}\nPercent of digits is: {digits}\nPercents of special symbols is: {spec_symbols}".format(letters=result['Letters'], digits = result['Digits'], spec_symbols = result['Spec_symbols'])