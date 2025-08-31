# Created by woxQAQ at 2025/08/31 15:15
# leetgo: 1.4.13
# https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) // 2 + 1
        while l < r - 1:
            k = (l + r) // 2
            if all(nums[i] * 2 <= nums[-k + i] for i in range(k)):
                l = k
            else:
                r = k
        return l * 2


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxNumOfMarkedIndices(nums)
    print("\noutput:", serialize(ans, "integer"))
