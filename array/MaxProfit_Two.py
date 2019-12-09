def max_profit_two(prices: list) -> int:
    i = 0
    valley = prices[0]
    peak = prices[0]
    max_profit = 0
    while i < len(prices) - 1:
        while i < len(prices) - 1 and prices[i] >= prices[i+1]:
            i += 1
        valley = prices[i]
        while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
            i += 1
        peak = prices[i]
        max_profit += peak - valley
    return max_profit


def max_profit_third(prices: list) -> int:
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]
    return max_profit


# price_list = [7, 1, 5, 3, 6, 4]
price_list = [1, 2, 3, 4, 5]
# print(max_profit_two(price_list))
print(max_profit_third(price_list))

