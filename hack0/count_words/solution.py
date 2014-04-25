def count_words(arr):
	count = {}
	for word in arr:
		if word in count:
			count[word] += 1
		else:
			count[word] = 1
	return count