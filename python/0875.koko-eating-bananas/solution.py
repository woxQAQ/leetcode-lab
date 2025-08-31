# Created by woxQAQ at 2025/08/31 14:06
# leetgo: 1.4.13
# https://leetcode.cn/problems/koko-eating-bananas/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)

        def helper(k):
            return sum((p - 1) // k + 1 for p in piles)

        n = len(piles)
        while l < r - 1:
            m = (l + r) // 2
            if helper(m) <= h:
                r = m
            else:
                l = m
        return r


# @lc code=end

if __name__ == "__main__":
    piles: List[int] = deserialize("List[int]", read_line())
    h: int = deserialize("int", read_line())
    ans = Solution().minEatingSpeed(piles, h)
    print("\noutput:", serialize(ans, "integer"))
