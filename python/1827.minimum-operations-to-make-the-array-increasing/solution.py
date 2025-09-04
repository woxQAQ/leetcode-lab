# Created by woxQAQ at 2025/09/04 13:47
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimum-operations-to-make-the-array-increasing/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        last = nums[0]
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] <= last:
                ans += last - nums[i] + 1
                nums[i] = last + 1
            last = nums[i]
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minOperations(nums)
    print("\noutput:", serialize(ans, "integer"))
