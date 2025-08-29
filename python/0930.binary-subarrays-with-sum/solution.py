# Created by woxQAQ at 2025/08/29 19:00
# leetgo: 1.4.15
# https://leetcode.cn/problems/binary-subarrays-with-sum/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def func(k):
            ans = l = 0
            temp = 0
            for r, x in enumerate(nums):
                temp += x
                while l <= r and temp >= k:
                    temp -= nums[l]
                    l += 1
                ans += l
            return ans

        upper, lower = func(goal), func(goal + 1)
        return upper - (lower if goal + 1 >= 0 else upper)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    goal: int = deserialize("int", read_line())
    ans = Solution().numSubarraysWithSum(nums, goal)
    print("\noutput:", serialize(ans, "integer"))
