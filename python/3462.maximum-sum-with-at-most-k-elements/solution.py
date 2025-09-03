# Created by woxQAQ at 2025/09/02 16:25
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximum-sum-with-at-most-k-elements/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        a = []
        for row, limit in zip(grid, limits):
            row.sort(reverse=True)
            a.extend(row[:limit])
        a.sort(reverse=True)
        return sum(a[:k])


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    limits: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxSum(grid, limits, k)
    print("\noutput:", serialize(ans, "long"))
