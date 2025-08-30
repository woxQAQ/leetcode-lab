# Created by woxQAQ at 2025/08/31 03:57
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimum-absolute-sum-difference/

from bisect import bisect, bisect_left
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        # [1,7,5],[2,3,5]
        # [1,4,0]
        #
        diffs = [abs(x - y) for x, y in zip(nums1, nums2)]
        snum1 = sorted(nums1)
        temp = 0
        for x, y in zip(nums1, nums2):
            i = bisect_left(snum1, y)
            curdiff = abs(x - y)
            if i < len(nums1):
                temp = max(temp, curdiff - abs(snum1[i] - y))
            if i > 0:
                temp = max(temp, curdiff - abs(snum1[i - 1] - y))
        return (sum(diffs) - temp) % (10**9 + 7)


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minAbsoluteSumDiff(nums1, nums2)
    print("\noutput:", serialize(ans, "integer"))
