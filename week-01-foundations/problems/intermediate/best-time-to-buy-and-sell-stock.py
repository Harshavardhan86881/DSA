"""Solution for 'Best Time to Buy and Sell Stock'. O(n) time, O(1) space."""


def max_profit(prices: list[int]) -> int:
    if not prices:
        return 0
    cheapest = prices[0]
    best = 0
    for price in prices[1:]:
        if price < cheapest:
            cheapest = price
        else:
            profit = price - cheapest
            if profit > best:
                best = profit
    return best


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
