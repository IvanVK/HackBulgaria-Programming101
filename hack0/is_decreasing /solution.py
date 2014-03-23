def is_decreasing(seq):
    a = len(seq)
    for i in range(1, a):
        if seq[i - 1] <= seq[i]:
            return False
    return True