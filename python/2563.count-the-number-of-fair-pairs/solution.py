# Created by woxQAQ at 2025/08/30 17:03
# leetgo: 1.4.13
# https://leetcode.cn/problems/count-the-number-of-fair-pairs/

from bisect import bisect_left
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        for i, x in enumerate(nums):
            # lower - x <= nums[j] <= upper - x
            iupper = bisect_left(nums, upper - x + 1, 0, i)
            ilow = bisect_left(nums, lower - x, 0, i)
            res += iupper - ilow
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    lower: int = deserialize("int", read_line())
    upper: int = deserialize("int", read_line())
    ans = Solution().countFairPairs(nums, lower, upper)
    print("\noutput:", serialize(ans, "long"))
