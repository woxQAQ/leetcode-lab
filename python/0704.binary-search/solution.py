# Created by woxQAQ at 2025/08/29 21:10
# leetgo: 1.4.15
# https://leetcode.cn/problems/binary-search/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = -1, len(nums)
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        return r if r < len(nums) and nums[r] == target else -1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().search(nums, target)
    print("\noutput:", serialize(ans, "integer"))
