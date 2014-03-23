def calculate_coins(sum):
    coins = [1, 2, 5, 10, 20, 50, 100]
    min_number = {}
    sum *= 100
    for coin in coins:
            count = 0
            while sum - coin >= 0:
                    count += 1
                    sum -= coin
            min_number[coin] = count
    return min_number