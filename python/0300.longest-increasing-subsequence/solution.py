# Created by woxQAQ at 2025/08/31 18:05
# leetgo: 1.4.13
# https://leetcode.cn/problems/longest-increasing-subsequence/

from functools import cache
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(i):
            res = 0
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    res = max(res, dfs(j))
            return res + 1

        return max(dfs(i) for i in range(n))


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().lengthOfLIS(nums)
    print("\noutput:", serialize(ans, "integer"))
