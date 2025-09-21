# Created by woxQAQ at 2025/09/20 17:32
# leetgo: 1.4.15
# https://leetcode.cn/problems/coin-change/

from functools import cache
from typing import *
from leetgo_py import *
from math import inf

# @lc code=begin


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # @cache
        # def dfs(i, j):
        #     if i == -1:
        #         return 0 if j == 0 else float("inf")
        #     if j < coins[i]:
        #         return dfs(i - 1, j)
        #     return min(dfs(i - 1, j), dfs(i, j - coins[i]) + 1)

        # res = dfs(len(coins) - 1, amount)
        # return res if res != float("inf") else -1
        dp = [[inf] * (amount + 1) for _ in range(len(coins) + 1)]
        dp[0][0] = 0
        for i, coin in enumerate(coins):
            for j in range(amount + 1):
                if j < coin:
                    dp[i + 1][j] = dp[i][j]
                else:
                    dp[i + 1][j] = min(dp[i][j], dp[i + 1][j - coin] + 1)

        return dp[-1][-1] if dp[-1][-1] != inf else -1


# @lc code=end

if __name__ == "__main__":
    coins: List[int] = deserialize("List[int]", read_line())
    amount: int = deserialize("int", read_line())
    ans = Solution().coinChange(coins, amount)
    print("\noutput:", serialize(ans, "integer"))
