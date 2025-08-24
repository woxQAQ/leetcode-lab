# Created by woxQAQ at 2025/08/24 17:58
# leetgo: 1.4.15
# https://leetcode.cn/problems/median-of-two-sorted-arrays/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findMedianSortedArrays(nums1, nums2)
    print("\noutput:", serialize(ans, "double"))
