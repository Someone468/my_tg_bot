import random

def coin_flip():
    coin_result = random.randint(0, 1)
    coin = ''
    if coin_result == 0:
        coin = 'Орёл'
    if coin_result == 1:
        coin = 'Решка'
    return coin
