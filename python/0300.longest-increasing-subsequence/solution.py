# Created by woxQAQ at 2025/09/20 17:18
# leetgo: 1.4.15
# https://leetcode.cn/problems/longest-increasing-subsequence/

from functools import cache
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dfs(i): LIS of nums[:i]
        @cache
        def dfs(i):
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j) + 1)
            return res

        return max(dfs(i) + 1 for i in range(len(nums)))


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().lengthOfLIS(nums)
    print("\noutput:", serialize(ans, "integer"))
