# Created by woxQAQ at 2025/08/31 17:53
# leetgo: 1.4.13
# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = -1, len(nums) - 1
        while l < r - 1:
            mid = (l + r) // 2
            if nums[mid] < nums[-1]:
                r = mid
            else:
                l = mid
        return nums[r]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findMin(nums)
    print("\noutput:", serialize(ans, "integer"))
