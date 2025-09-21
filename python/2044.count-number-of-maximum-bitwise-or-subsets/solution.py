# Created by woxQAQ at 2025/09/20 21:29
# leetgo: 1.4.15
# https://leetcode.cn/problems/count-number-of-maximum-bitwise-or-subsets/

from functools import reduce
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        total = reduce(lambda x, y: x | y, nums)
        ans = 0

        def dfs(i, st):
            if st == total:
                nonlocal ans
                ans += 1 << (len(nums) - i)
                return
            if i == len(nums):
                return
            dfs(i + 1, st | nums[i])
            dfs(i + 1, st)

        dfs(0, 0)
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countMaxOrSubsets(nums)
    print("\noutput:", serialize(ans, "integer"))
