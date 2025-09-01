# Created by woxQAQ at 2025/09/01 12:40
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximum-points-inside-the-square/

from bisect import bisect, bisect_left
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        ans = 0

        def check(m):
            vis = set()
            for (x, y), label in zip(points, s):
                if abs(x) <= m and abs(y) <= m:
                    if label in vis:
                        return True
                    vis.add(label)
            nonlocal ans
            ans = len(vis)
            return False

        l = -1
        r = 1_000_000_001
        while l < r - 1:
            m = (l + r) // 2
            if not check(m):
                l = m
            else:
                r = m

        return ans


# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    s: str = deserialize("str", read_line())
    ans = Solution().maxPointsInsideSquare(points, s)
    print("\noutput:", serialize(ans, "integer"))
