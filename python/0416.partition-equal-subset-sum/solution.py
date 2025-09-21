# Created by woxQAQ at 2025/09/20 17:10
# leetgo: 1.4.15
# https://leetcode.cn/problems/partition-equal-subset-sum/

from functools import cache
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        @cache
        def dfs(i, cur):
            if i == len(nums):
                return cur == target
            return dfs(i + 1, cur + nums[i]) or dfs(i + 1, cur)

        return dfs(0, 0)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canPartition(nums)
    print("\noutput:", serialize(ans, "boolean"))
