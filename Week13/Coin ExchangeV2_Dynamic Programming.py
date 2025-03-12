def coin_exchange(amount: int, coins: dict):
    """Function using Dynamic Programming to minimize the number of coins."""
    print(f"Amount: {amount}")

    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    sorted_coins = sorted(coins.keys(), key=int, reverse=True)

    for i in range(1, amount + 1):
        for coin in sorted_coins:
            c = int(coin)
            if i >= c and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1
                coin_used[i] = c

    result = {}
    remaining = amount
    while remaining > 0:
        c = coin_used[remaining]
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
        remaining -= c

    print("Coin exchange result:")
    total_coins = 0
    for coin in sorted_coins:
        count = result.get(int(coin), 0)
        print(f"  {coin} baht = {count} coins")
        total_coins += count

    print(f"Number of coins: {total_coins}")


def convert_key(data):
    """Convert String key to integer"""
    return {int(k): v for k, v in data.items()}


def main():
    """Main function"""
    import json

    coin_exchange(int(input()), convert_key(json.loads(input())))


main()
