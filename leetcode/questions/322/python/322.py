from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float('inf')
        dp = [INF for _ in range(amount + 1)]
        dp[amount] = 0

        for cur_amount in reversed(range(amount + 1)):
            for coin in coins:
                if cur_amount + coin <= amount:
                    dp[cur_amount] = min(dp[cur_amount], dp[cur_amount + coin] + 1)

        return dp[0] if dp[0] != INF else -1