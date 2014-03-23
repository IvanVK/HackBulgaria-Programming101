def number_to_list(n):
	toStr = str(n)
	lst = list(toStr)
	new = ",".join(toStr)
	print ("[" + new + "]")