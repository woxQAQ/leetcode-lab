# Created by woxQAQ at 2025/09/02 15:13
# leetgo: 1.4.13
# https://leetcode.cn/problems/rearrange-array-to-maximize-prefix-score/

from typing import *
from leetgo_py import *
from itertools import accumulate

# @lc code=begin


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return sum(s > 0 for s in accumulate(nums))


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxScore(nums)
    print("\noutput:", serialize(ans, "integer"))
