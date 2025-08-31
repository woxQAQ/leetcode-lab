# Created by woxQAQ at 2025/08/31 19:51
# leetgo: 1.4.13
# https://leetcode.cn/problems/furthest-building-you-can-reach/

from typing import *
from typing_extensions import Reader
from leetgo_py import *

# @lc code=begin


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        def check(mid):
            need = [heights[i + 1] - heights[i] for i in range(mid)]
            need.sort(reverse=True)
            for i in range(ladders):
                if i < mid:
                    need[i] = 0
            return sum(d for d in need if d > 0) <= bricks

        l, r = -1, len(heights)
        while l < r - 1:
            m = (l + r) // 2
            if check(m):
                l = m
            else:
                r = m

        return l


# @lc code=end

if __name__ == "__main__":
    heights: List[int] = deserialize("List[int]", read_line())
    bricks: int = deserialize("int", read_line())
    ladders: int = deserialize("int", read_line())
    ans = Solution().furthestBuilding(heights, bricks, ladders)
    print("\noutput:", serialize(ans, "integer"))
