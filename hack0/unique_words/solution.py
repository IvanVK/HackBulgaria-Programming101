def count_words(arr):
	count = {}
	for word in arr:
		if word in count:
			count[word] += 1
		else:
			count[word] = 1
	return count

def unique_words_count(arr):
	return len(count_words(arr))
			