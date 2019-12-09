import sys


def max_profit(prices: list) -> int:
    min_price = sys.maxsize
    max_result = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_result:
            max_result = prices[i] - min_price
    return max_result


# price_list = [7, 1, 5, 3, 6, 4]
# price_list = [1, 2, 3, 4, 5]
# print(max_profit(price_list))

assert max_profit([7, 1, 5, 3, 6, 4]) == 5, "First"
assert max_profit([7, 6, 4, 3, 1]) == 0, "Second"

