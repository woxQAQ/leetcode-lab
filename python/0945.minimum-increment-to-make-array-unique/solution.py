# Created by woxQAQ at 2025/09/03 07:21
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimum-increment-to-make-array-unique/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        # 1,1,2,2,3,7
        #
        prev = nums[0]
        res = 0
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                res += prev + 1 - nums[i]
            prev = max(prev + 1, nums[i])
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minIncrementForUnique(nums)
    print("\noutput:", serialize(ans, "integer"))
