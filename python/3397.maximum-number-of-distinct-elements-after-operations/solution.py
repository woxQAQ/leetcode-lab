# Created by woxQAQ at 2025/09/03 09:46
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximum-number-of-distinct-elements-after-operations/

from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        # 0,1,2,3,4,5
        nums.sort()
        ans = 0
        prev = -inf
        for x in nums:
            x = min(x + k, max(x - k, prev + 1))
            if x > prev:
                ans += 1
                prev = x
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxDistinctElements(nums, k)
    print("\noutput:", serialize(ans, "integer"))
