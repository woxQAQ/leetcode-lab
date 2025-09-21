# Created by woxQAQ at 2025/09/20 17:13
# leetgo: 1.4.15
# https://leetcode.cn/problems/maximum-product-subarray/

from functools import cache
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        _max = _min = nums[0]

        @cache
        def dfs(i):
            if i == 0:
                return nums[0]
            nonlocal _max, _min
            _max = max(dfs(i - 1) * nums[i], _min * nums[i], nums[i])
            _min = min(dfs(i - 1) * nums[i], _min * nums[i], nums[i])
            return _max

        return max(dfs(i) for i in range(len(nums)))


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProduct(nums)
    print("\noutput:", serialize(ans, "integer"))
