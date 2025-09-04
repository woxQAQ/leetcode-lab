# Created by woxQAQ at 2025/09/04 08:27
# leetgo: 1.4.13
# https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, (len(nums) + 1) // 2
        while r < len(nums):
            if nums[l] * 2 <= nums[r]:
                l += 1
            r += 1
        return l * 2


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxNumOfMarkedIndices(nums)
    print("\noutput:", serialize(ans, "integer"))
