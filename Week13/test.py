"""Coin exchange with dynamic programming"""


def min_coin(m: int, coins: list):
    """Minimum coins for exchange using dynamic programming"""

    memo = {}
    memo[0] = 0
    for i in range(1, m + 1):
        for coin in coins:
            subproblem = i - coin
            if subproblem >= 0:
                memo[i] = min(
                    memo.get(i, float("inf")), memo.get(subproblem, float("inf")) + 1
                )

    return memo[m]


print(min_coin(135, [10, 5, 2, 1]))
