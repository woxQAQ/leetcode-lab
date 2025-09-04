# Created by woxQAQ at 2025/09/03 21:16
# leetgo: 1.4.13
# https://leetcode.cn/problems/array-partition/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().arrayPairSum(nums)
    print("\noutput:", serialize(ans, "integer"))
