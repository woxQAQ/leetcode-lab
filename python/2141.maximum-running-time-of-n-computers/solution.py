# Created by woxQAQ at 2025/09/01 12:25
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximum-running-time-of-n-computers/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # m
        # m * n
        l, r = 0, sum(batteries) // n + 1
        while l < r - 1:
            m = (l + r) // 2
            if sum(min(m, b) for b in batteries) >= m * n:
                l = m
            else:
                r = m
        return l


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    batteries: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxRunTime(n, batteries)
    print("\noutput:", serialize(ans, "long"))
