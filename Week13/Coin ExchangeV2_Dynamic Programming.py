"""Coin exhange with dynamic programming"""


def coin_exchangeV2(amount: int, coins: dict):
    """Dynamic Programming Tabulation + Knapsack Approach"""
    max_value = amount + 1
    dp = [max_value] * (amount + 1)
    track = [-1] * (amount + 1)
    dp[0] = 0

    coin_list = sorted(coins.keys(), key=int, reverse=True)
    coin_list = [int(c) for c in coin_list]

    for coin in coin_list:
        coin = int(coin)
        count = coins[coin]
        for _ in range(count):
            for i in range(amount, coin - 1, -1):
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    track[i] = coin

    if dp[amount] == max_value:
        print("Can not exchange.")
        return

    coin_count = {c: 0 for c in coin_list}
    remaining = amount
    while remaining > 0:
        coin = track[remaining]
        if coin == -1:
            print("Can not exchange.")
            return
        coin_count[coin] += 1
        remaining -= coin

    print(f"Amount: {amount}")
    print("Coin exchange result:")
    total_coins = 0
    for coin in sorted(coin_list, reverse=True):
        count = coin_count.get(coin, 0)
        print(f"  {coin} baht = {count} coins")
        total_coins += count
    print(f"Number of coins: {total_coins}")


def convert_key(data):
    """Convert String key to integer"""
    return {int(k): v for k, v in data.items()}


def main():
    """Main function"""
    import json

    coin_exchangeV2(int(input()), convert_key(json.loads(input())))


main()
