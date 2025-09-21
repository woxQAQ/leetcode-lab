# Created by woxQAQ at 2025/09/20 17:53
# leetgo: 1.4.15
# https://leetcode.cn/problems/longest-common-subsequence/

from functools import cache
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return dfs(i - 1, j - 1) + 1
            return max(dfs(i - 1, j), dfs(i, j - 1))

        return dfs(len(text1) - 1, len(text2) - 1)


# @lc code=end

if __name__ == "__main__":
    text1: str = deserialize("str", read_line())
    text2: str = deserialize("str", read_line())
    ans = Solution().longestCommonSubsequence(text1, text2)
    print("\noutput:", serialize(ans, "integer"))
