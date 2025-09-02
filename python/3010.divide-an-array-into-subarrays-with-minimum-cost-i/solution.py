# Created by woxQAQ at 2025/09/02 14:01
# leetgo: 1.4.13
# https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

from math import inf
from typing import *
from leetgo_py import *
from heapq import nsmallest

# @lc code=begin


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        f0, f1 = inf, inf
        for x in nums[1:]:
            if x < f0:
                f1 = f0
                f0 = x
            elif x < f1:
                f1 = x
        return nums[0] + f0 + f1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumCost(nums)
    print("\noutput:", serialize(ans, "integer"))
