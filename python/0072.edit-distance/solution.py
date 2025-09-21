# Created by woxQAQ at 2025/09/20 17:47
# leetgo: 1.4.15
# https://leetcode.cn/problems/edit-distance/

from functools import cache
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0] = list(range(m + 1))
        for i in range(1, n + 1):
            dp[i][0] = i
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = (
                        min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    )
        return dp[n][m]
        # @cache
        # def dfs(i, j):
        #     if i < 0:
        #         return j + 1
        #     if j < 0:
        #         return i + 1
        #     if word1[i] == word2[j]:
        #         return dfs(i - 1, j - 1)
        #     return min(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1)) + 1

        # return dfs(len(word1) - 1, len(word2) - 1)


# @lc code=end

if __name__ == "__main__":
    word1: str = deserialize("str", read_line())
    word2: str = deserialize("str", read_line())
    ans = Solution().minDistance(word1, word2)
    print("\noutput:", serialize(ans, "integer"))
