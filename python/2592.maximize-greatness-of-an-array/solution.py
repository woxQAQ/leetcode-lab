# Created by woxQAQ at 2025/09/04 07:57
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximize-greatness-of-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        # nums[i] 越大，越难perm[i] > nums[i]
        # nums[j] 被 nums[i] 消费后
        nums.sort()
        # 1,1,1,2,3,3,5

        ans = 0
        for num in nums:
            if num > nums[ans]:
                ans += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximizeGreatness(nums)
    print("\noutput:", serialize(ans, "integer"))
