def count_consonants(string):
	count = 0
	cons = "bcdfghjklmnpqrstvwxz"
	for letter in string:
		if letter.lower() in cons:
			count += 1
	return count
