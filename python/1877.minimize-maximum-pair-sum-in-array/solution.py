# Created by woxQAQ at 2025/09/03 21:18
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimize-maximum-pair-sum-in-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # 1,2,7,8,8,9
        nums.sort()
        return max(nums[i] + nums[-i - 1] for i in range(len(nums) // 2))


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minPairSum(nums)
    print("\noutput:", serialize(ans, "integer"))
