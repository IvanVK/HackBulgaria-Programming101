def div(n):
    i = 1
    list = []
    while i <= n:
        if n % i == 0:
            list.append(i)
        i = i + 1
    return list

def sum_of_divisors(n):
 return sum(div(n))
