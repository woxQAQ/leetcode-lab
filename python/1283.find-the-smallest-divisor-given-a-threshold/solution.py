# Created by woxQAQ at 2025/08/31 15:19
# leetgo: 1.4.13
# https://leetcode.cn/problems/find-the-smallest-divisor-given-a-threshold/

from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # k,
        #  ⌈a/b⌉ = 1+ ⌊(a-1)/b⌋
        # sum(⌈nunm[i]//k⌉) = sum(⌈(nums[i]-1)//k⌉ + 1) =sum(⌈(nums[i]-1)//k⌉) + n
        l, r = 0, max(nums)
        while l < r - 1:
            mid = (l + r) // 2
            if sum((x - 1) // mid for x in nums) + len(nums) <= threshold:
                r = mid
            else:
                l = mid
        return r


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    threshold: int = deserialize("int", read_line())
    ans = Solution().smallestDivisor(nums, threshold)
    print("\noutput:", serialize(ans, "integer"))
