# Created by woxQAQ at 2025/08/31 13:15
# leetgo: 1.4.13
# https://leetcode.cn/problems/sqrtx/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def mySqrt(self, x: int) -> int:
        # sqrt * sqrt = x
        l, r = 0, x + 1
        while l < r - 1:
            m = (l + r) // 2
            if m * m <= x:
                l = m
            else:
                r = m
        return l


# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    ans = Solution().mySqrt(x)
    print("\noutput:", serialize(ans, "integer"))
