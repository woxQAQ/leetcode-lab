# Created by woxQAQ at 2026/03/12 08:26
# leetgo: 1.4.16
# https://leetcode.cn/problems/maximum-subarray/
from math import inf

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        pre_sum = 0
        min_pre_sum = 0
        for x in nums:
            pre_sum += x
            ans = max(ans,pre_sum-min_pre_sum)
            min_pre_sum = min(min_pre_sum,pre_sum)
        return ans

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSubArray(nums)
    print("\noutput:", serialize(ans, "integer"))
