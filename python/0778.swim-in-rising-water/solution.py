# Created by woxQAQ at 2025/09/01 20:05
# leetgo: 1.4.13
# https://leetcode.cn/problems/swim-in-rising-water/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().swimInWater(grid)
    print("\noutput:", serialize(ans, "integer"))
