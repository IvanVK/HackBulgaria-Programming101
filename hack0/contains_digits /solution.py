def contains_digits(number, digits):
	str_number = str(number)
	for digit in digits:
		if not(str(digit) in str_number):
			return False
	return True