# Created by woxQAQ at 2025/09/04 16:52
# leetgo: 1.4.15
# https://leetcode.cn/problems/jump-game/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r = 0
        for i in range(len(nums) - 1):
            if r < nums[i] + i:
                r = nums[i] + i
            if nums[i] == 0 and r <= i:
                return False
        return True


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canJump(nums)
    print("\noutput:", serialize(ans, "boolean"))
