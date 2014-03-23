def sum_of_digits(n):
 sums = 0
 while n != 0:
  sums += int(n % 10)
  n /= 10
 return sums
 
