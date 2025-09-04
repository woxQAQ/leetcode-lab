# Created by woxQAQ at 2025/09/04 13:38
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # [1,0,0,1,0,0]
        l = 0

        def reverse(i):
            for j in range(0, 3):
                if nums[i + j]:
                    nums[i + j] = 0
                else:
                    nums[i + j] = 1

        res = 0
        while l < len(nums) - 2:
            if nums[l]:
                l += 1
            else:
                reverse(l)
                res += 1
                for _ in range(1, 3):
                    if not nums[l]:
                        break
                    l += 1
        return res if 0 not in nums else -1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minOperations(nums)
    print("\noutput:", serialize(ans, "integer"))
