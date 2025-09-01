# Created by woxQAQ at 2025/09/01 19:41
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimize-maximum-of-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        l = 0
        r = max(nums)
        n = len(nums)

        def check(mid):
            carry = 0
            for i in range(n - 1, 0, -1):
                carry = max(nums[i] + carry - mid, 0)
            return carry + nums[0] <= mid

        while l < r - 1:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m
        return r


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimizeArrayValue(nums)
    print("\noutput:", serialize(ans, "integer"))
