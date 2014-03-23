def is_int_palindrom(n):
 a = str(n)
 if a[:1] == a[-1:][::-1]:
  return True
 else:
  return False
