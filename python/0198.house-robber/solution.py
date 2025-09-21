# Created by woxQAQ at 2025/09/20 17:43
# leetgo: 1.4.15
# https://leetcode.cn/problems/house-robber/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def rob(self, nums: List[int]) -> int:
        # def dfs(i):
        #     if i < 0:
        #         return 0
        #     return max(dfs(i - 1), dfs(i - 2) + nums[i])

        # return dfs(len(nums) - 1)
        # dp = [0] * (len(nums) + 1)
        # dp[1] = nums[0]
        # for i in range(2, len(nums) + 1):
        #     dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        # return dp[-1]
        f0 = 0
        f1 = nums[0]
        for i in range(2, len(nums) + 1):
            f0, f1 = f1, max(f1, f0 + nums[i - 1])
        return f1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().rob(nums)
    print("\noutput:", serialize(ans, "integer"))
