# Created by woxQAQ at 2025/09/03 12:53
# leetgo: 1.4.13
# https://leetcode.cn/problems/greatest-sum-divisible-by-three/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        s = sum(nums)
        if s % 3 == 0:
            return s
        n1, n2 = (
            sorted([num for num in nums if num % 3 == 1]),
            sorted([num for num in nums if num % 3 == 2]),
        )
        if s % 3 == 2:
            n1, n2 = n2, n1
        ans = s - n1[0] if n1 else 0
        if len(n2) > 1:
            ans = max(ans, s - n2[0] - n2[1])
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSumDivThree(nums)
    print("\noutput:", serialize(ans, "integer"))
