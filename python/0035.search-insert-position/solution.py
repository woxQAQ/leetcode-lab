# Created by woxQAQ at 2025/08/29 21:06
# leetgo: 1.4.15
# https://leetcode.cn/problems/search-insert-position/

from bisect import bisect_left
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().searchInsert(nums, target)
    print("\noutput:", serialize(ans, "integer"))
