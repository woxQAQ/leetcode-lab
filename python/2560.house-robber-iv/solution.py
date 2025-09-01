# Created by woxQAQ at 2025/09/01 19:54
# leetgo: 1.4.13
# https://leetcode.cn/problems/house-robber-iv/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l, r = 0, max(nums)

        def check(mid):
            f0 = f1 = 0
            for num in nums:
                if num > mid:
                    f0 = f1
                else:
                    f0, f1 = f1, max(f1, f0 + 1)
            return f1 >= k

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
    k: int = deserialize("int", read_line())
    ans = Solution().minCapability(nums, k)
    print("\noutput:", serialize(ans, "integer"))
