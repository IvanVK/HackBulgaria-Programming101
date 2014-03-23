def count_vowels(string):
 count = 0
 vowels = "aeiouyAEIOUY"
 for letter in string:
  if letter in vowels:
   count += 1
 return count
