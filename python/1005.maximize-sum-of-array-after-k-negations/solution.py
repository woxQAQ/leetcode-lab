# Created by woxQAQ at 2025/09/02 13:16
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i, x in enumerate(nums):
            if k == 0 or x >= 0:
                break
            nums[i] *= -1
            k -= 1
        return sum(nums) - min(nums) * (k % 2 * 2)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().largestSumAfterKNegations(nums, k)
    print("\noutput:", serialize(ans, "integer"))
