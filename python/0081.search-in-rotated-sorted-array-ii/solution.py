# Created by woxQAQ at 2025/09/19 17:50
# leetgo: 1.4.15
# https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = -1, len(nums) - 1

        def check(m):
            v = nums[m]
            if v > nums[r]:
                return target > nums[r] and v >= target
            return target > nums[r] or v >= target

        while l < r - 1:
            mid = (l + r) // 2
            if nums[mid] == nums[r]:
                r -= 1
            elif check(mid):
                r = mid
            else:
                l = mid
        return nums[r] == target


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().search(nums, target)
    print("\noutput:", serialize(ans, "boolean"))
