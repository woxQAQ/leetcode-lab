# Created by woxQAQ at 2025/09/01 19:03
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimum-limit-of-balls-in-a-bag/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # 最小开销为 m，那么，
        # 对于 x = nums[i],分为 k 个袋子
        # m*k >= x
        # k >= x / m
        # op_count = k-1
        l, r = 0, max(nums)
        while l < r - 1:
            m = (l + r) // 2
            if sum((x - 1 + m) // m - 1 for x in nums) <= maxOperations:
                r = m
            else:
                l = m
        return r


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    maxOperations: int = deserialize("int", read_line())
    ans = Solution().minimumSize(nums, maxOperations)
    print("\noutput:", serialize(ans, "integer"))
