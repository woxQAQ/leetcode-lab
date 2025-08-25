# Created by woxQAQ at 2025/08/24 17:59
# leetgo: 1.4.15
# https://leetcode.cn/problems/longest-palindromic-substring/

from typing import *
from leetgo_py import *
from functools import cache

# @lc code=begin


class Solution:
    def longestPalindrome(self, s: str) -> str:
        @cache
        def expand_around_center(l, r):
            while l >= 0 and l < len(s) and r >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        if not s:
            return ""
        l, r = 0, 0
        for i in range(len(s)):
            l1, r1 = expand_around_center(i, i)
            l2, r2 = expand_around_center(i, i + 1)
            if r1 - l1 > r - l:
                l, r = l1, r1
            if r2 - l2 > r - l:
                l, r = l2, r2
        return s[l : r + 1]


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().longestPalindrome(s)
    print("\noutput:", serialize(ans, "string"))
