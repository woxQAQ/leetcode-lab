# Created by woxQAQ at 2025/08/31 19:00
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximum-value-at-a-given-index-in-a-bounded-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # 4,2,6
        # [1,1,2,3,3,3,4,3,2,1],
        #              ^
        def check(k):
            h = k - 1
            l = index
            if l <= h:
                lsum = l * (2 * h - l + 1) // 2
            else:
                lsum = (h + 1) * h // 2 + (l - h)
            r = n - index - 1
            if r <= h:
                rsum = r * (2 * h - r + 1) // 2
            else:
                rsum = (h + 1) * h // 2 + (r - h)
            return lsum + rsum + k <= maxSum

        l, r = 0, maxSum + 1
        while l < r - 1:
            m = (l + r) // 2
            if check(m):
                l = m
            else:
                r = m
        return l


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    index: int = deserialize("int", read_line())
    maxSum: int = deserialize("int", read_line())
    ans = Solution().maxValue(n, index, maxSum)
    print("\noutput:", serialize(ans, "integer"))
