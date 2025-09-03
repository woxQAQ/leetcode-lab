# Created by woxQAQ at 2025/09/03 09:35
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 4:
            # 直接全部改为相同的数
            return 0
        nums.sort()
        # 0,1,5,10,14
        # 2,3,4,5
        #
        # nums[-1,-2,-3] -> nums[-4]
        # nums[0,1,2] -> num[3]
        # nums[-1,-2] -> nums[-3],nums[0] -> nums[1]
        # nums[-1] -> nums[-2], nums[1,2] -> nums[3]
        # nums[-1] -> nums[-2], nums[1,2,3] -> nums[4]
        return min(
            nums[-1] - nums[3],
            nums[-2] - nums[2],
            nums[-3] - nums[1],
            nums[-4] - nums[0],
        )


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minDifference(nums)
    print("\noutput:", serialize(ans, "integer"))
