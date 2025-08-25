# Created by woxQAQ at 2025/08/24 01:31
# leetgo: 1.4.15
# https://leetcode.cn/problems/ones-and-zeroes/

from functools import cache
from typing import *

from leetgo_py import *

# @lc code=begin


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """

        每次操作？选择 strs[i] 或则不选择
            - 不选择？容量不变
            - 选择？1背包容量 - count(1,str[i]) 0背包容量 - count(0,str[i])


        子问题：在 strs[0:i+1] 中,最多有 j 个 0 和 k 个 1 的最大子集长度
        下一个子问题：
            - 不选择？在 str[0:i] 中，找到最多有 有 j 个 0 和 k 个 1 的最大子集长度
            - 选择？....

        define dfs(i,j,k)

        corner:
            - dfs(-1,*,*)=0


        answer = dfs(len(strs),m,n)
        """

        @cache
        def count(i):
            counter = Counter(strs[i])
            return counter["0"], counter["1"]

        # @cache
        # def dfs(i,j,k):
        #     if i < 0:
        #         return 0
        #     ans = dfs(i-1,j,k)
        #     c0,c1 = count(i)
        #     if j >= c0 and k >= c1:
        #         ans = max(ans,dfs(i-1,j-c0,k-c1)+1)
        #     return ans
        # return dfs(len(strs)-1,m,n)
        #
        # dp = [[[0] * (n+1) for _ in range(m+1)] for _ in range(len(strs)+1)]
        # for i in range(len(strs)+1):
        #     for j in range(m+1):
        #         for k in range(n+1):
        #             if i == 0:
        #                 dp[i][j][k] = 0
        #             else:
        #                 c0,c1 = count(i-1)
        #                 dp[i][j][k] = dp[i-1][j][k]
        #                 if j >= c0 and k >= c1:
        #                     dp[i][j][k] = max(dp[i][j][k],dp[i-1][j-c0][k-c1]+1)
        # return dp[len(strs)][m][n]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(len(strs)):
            c0, c1 = count(i)
            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    if j >= c0 and k >= c1:
                        dp[j][k] = max(dp[j][k], dp[j - c0][k - c1] + 1)
        return dp[m][n]


# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().findMaxForm(strs, m, n)
    print("\noutput:", serialize(ans, "integer"))
