# Created by woxQAQ at 2025/08/31 13:22
# leetgo: 1.4.13
# https://leetcode.cn/problems/search-a-2d-matrix-ii/

from bisect import bisect_left
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) - 1
        while l < len(matrix) and r >= 0:
            if matrix[l][r] == target:
                return True
            elif matrix[l][r] < target:
                l += 1
            else:
                r -= 1
        return False


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().searchMatrix(matrix, target)
    print("\noutput:", serialize(ans, "boolean"))
