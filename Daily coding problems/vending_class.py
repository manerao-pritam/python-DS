"""
Interview question:
Make a class for vending machine which can dispence the coins (min no. of coins not required) for the amount
"""

from collections import Counter


class VendingMachine:
    coins = Counter()
    total = 0

    def __init__(self, coins) -> None:
        self.coins = Counter(coins)

        for coin, count in self.coins.items():
            self.total += coin * count

    def get_change(self, amt) -> dict({int: int}):
        if self.total < amt:
            return "Not enough money"

        coin_idx, sorted_coins = 0, sorted(self.coins)[::-1]
        running_sum = 0
        result = Counter()

        while amt >= running_sum and coin_idx < len(sorted_coins):
            max_coin = sorted_coins[coin_idx]

            while (
                max_coin <= (amt - running_sum)
                and result[max_coin] < self.coins[max_coin]
            ):
                running_sum += max_coin
                result[max_coin] += 1

            coin_idx += 1

        if running_sum != amt:
            return "Not enough money"

        for coin in result:
            self.coins[coin] -= result[coin]

            # all coins for this denomination were consumed
            if not self.coins[coin]:
                del self.coins[coin]

        return result


v1 = VendingMachine([1, 2, 3, 2, 3, 2, 2, 1, 2, 3, 2, 2, 100])
print(v1.coins)
print(v1.get_change(16))
print(v1.coins)
print(v1.get_change(6))
print(v1.coins)
print(v1.get_change(11))
print(v1.coins)
print(v1.get_change(101))
print(v1.coins)
print(v1.get_change(3))
print(v1.coins)