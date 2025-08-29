# Created by woxQAQ at 2025/08/29 20:52
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import *
from leetgo_py import *
from bisect import bisect_left, bisect_right

# @lc code=begin


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(target):
            l = -1
            r = len(nums)
            while l < r - 1:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid
                else:
                    r = mid
            return r

        start = search(target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = search(target + 1) - 1
        return [start, end]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().searchRange(nums, target)
    print("\noutput:", serialize(ans, "integer[]"))
