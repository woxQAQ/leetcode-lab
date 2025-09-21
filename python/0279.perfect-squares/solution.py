# Created by woxQAQ at 2025/09/20 17:39
# leetgo: 1.4.15
# https://leetcode.cn/problems/perfect-squares/

from functools import cache
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def numSquares(self, n: int) -> int:
        # @cache
        # def dfs(i):
        #     if i == 0:
        #         return 0
        #     res = float("inf")
        #     for j in range(1, int(i**0.5) + 1):
        #         res = min(res, dfs(i - j * j) + 1)
        #     return res

        # return dfs(n)
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(1, int(i**0.5) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().numSquares(n)
    print("\noutput:", serialize(ans, "integer"))
