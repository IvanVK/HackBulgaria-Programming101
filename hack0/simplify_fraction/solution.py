def simplify_fraction(fraction):
    p = 2
    while p <= fraction[0]:
        while fraction[0] % p == 0 and fraction[1] % p == 0:
            fraction = (int(fraction[0] / p), int(fraction[1] / p))
        p += 1
    return fraction