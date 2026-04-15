def min_coins(amount):
    coins = [25, 10, 5, 1]
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result

if __name__ == '__main__':
    amount = 63
    selected = min_coins(amount)
    print('Selected coins:', selected)
    print('Number of coins:', len(selected))
