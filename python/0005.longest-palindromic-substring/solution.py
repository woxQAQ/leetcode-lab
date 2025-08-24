# Created by woxQAQ at 2025/08/24 17:59
# leetgo: 1.4.15
# https://leetcode.cn/problems/longest-palindromic-substring/

from math import inf
from typing import *
from leetgo_py import *
from functools import cache

# @lc code=begin

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """

        """
        # @cache
        # def dfs(i,j):
        #     if i == j:
        #         return True
        #     if j == i+1:
        #         return s[i]==s[j]
        #     return s[i]==s[j] and dfs(i+1,j-1)
        n=len(s)
        l,r = 0,0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if dfs(i,j) and j-i>r-l:
        #             l,r = i,j
        # dfs.cache_clear()
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(n,-1,-1):
            for j in range(i+1,n):
                if j == i+1:
                    dp[i][j] = s[i]==s[j]
                else:
                    dp[i][j] = s[i]==s[j] and dp[i+1][j-1]
                if dp[i][j] and j-i>r-l:
                    l,r = i,j
        return s[l:r+1]
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().longestPalindrome(s)
    print("\noutput:", serialize(ans, "string"))
