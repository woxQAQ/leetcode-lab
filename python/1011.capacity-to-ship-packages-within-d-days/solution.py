# Created by woxQAQ at 2025/08/31 13:46
# leetgo: 1.4.13
# https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # ship * days >= weights
        l = max(weights) - 1
        r = sum(weights)

        def helper(load):
            day = 1
            s = 0
            for x in weights:
                s += x
                if s > load:
                    day += 1
                    s = x
            return day

        while l < r - 1:
            m = (l + r) // 2
            if helper(m) > days:
                l = m
            else:
                r = m
        return r


# @lc code=end

if __name__ == "__main__":
    weights: List[int] = deserialize("List[int]", read_line())
    days: int = deserialize("int", read_line())
    ans = Solution().shipWithinDays(weights, days)
    print("\noutput:", serialize(ans, "integer"))
