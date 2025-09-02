# Created by woxQAQ at 2025/09/02 15:18
# leetgo: 1.4.13
# https://leetcode.cn/problems/largest-perimeter-triangle/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # [10,2,1,1]
        nums.sort(reverse=True)
        for i in range(0, len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().largestPerimeter(nums)
    print("\noutput:", serialize(ans, "integer"))
