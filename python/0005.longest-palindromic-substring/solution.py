# Created by woxQAQ at 2025/09/20 17:55
# leetgo: 1.4.15
# https://leetcode.cn/problems/longest-palindromic-substring/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l, r

        start, end = 0, 0
        for i in range(len(s)):
            l1, r1 = helper(i, i)
            l2, r2 = helper(i, i + 1)
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        return s[start + 1 : end]


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().longestPalindrome(s)
    print("\noutput:", serialize(ans, "string"))
