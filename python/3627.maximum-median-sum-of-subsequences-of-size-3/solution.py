# Created by woxQAQ at 2025/09/02 16:19
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximum-median-sum-of-subsequences-of-size-3/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        # [3,3,2,2,1,1]
        #
        # 3 3 1
        # 2,2,1
        ans = 0
        l, r = 1, len(nums) - 1
        while l < r:
            ans += nums[l]
            l += 2
            r -= 1
        return ans
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumMedianSum(nums)
    print("\noutput:", serialize(ans, "long"))
