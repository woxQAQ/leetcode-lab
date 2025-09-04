# Created by woxQAQ at 2025/09/04 13:34
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimum-operations-to-make-columns-strictly-increasing/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        last = grid[0]
        res = 0
        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] <= last[j]:
                    res += last[j] - grid[i][j] + 1
                    grid[i][j] = last[j] + 1
                last[j] = grid[i][j]
        return res


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumOperations(grid)
    print("\noutput:", serialize(ans, "integer"))
