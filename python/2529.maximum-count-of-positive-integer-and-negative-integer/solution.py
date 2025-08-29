# Created by woxQAQ at 2025/08/29 21:37
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer/

from bisect import bisect_left
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        i, j = bisect_left(nums, 1), bisect_left(nums, 0)
        return max(j, len(nums) - i)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumCount(nums)
    print("\noutput:", serialize(ans, "integer"))
