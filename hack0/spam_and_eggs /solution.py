def prepare_meal(number):
    count = 0
    while number % 3 == 0:
        count += 1
        number /= 3
    spam = ' '.join(["spam"] * count)
    if number % 5 == 0:
        if count > 0:
            spam += ' and eggs'
        else:
            spam += 'eggs'
    return spam