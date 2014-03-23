def count_substrings(haystack, needle):
 start = 0
 count = 0
 while True :
  start = haystack.find(needle,start) + 1
  if start > 0: 
   count += 1
  else:
   return count
