# Created by woxQAQ at 2025/08/29 16:54
# leetgo: 1.4.15
# https://leetcode.cn/problems/subarray-product-less-than-k/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        l = ans = 0
        temp = 1
        for r, num in enumerate(nums):
            temp *= num
            while temp >= k:
                temp //= nums[l]
                l += 1
            ans += r - l + 1
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numSubarrayProductLessThanK(nums, k)
    print("\noutput:", serialize(ans, "integer"))
