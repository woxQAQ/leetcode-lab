# Created by woxQAQ at 2025/08/24 17:58
# leetgo: 1.4.15
# https://leetcode.cn/problems/median-of-two-sorted-arrays/

from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        def func(a, b):
            m, n = len(a), len(b)
            a = [-inf] + a + [inf]
            b = [-inf] + b + [inf]
            i, j = 0, (m + n + 1) // 2
            while True:
                if a[i] <= b[j + 1] and a[i + 1] > b[j]:
                    m1 = max(a[i], b[j])
                    m2 = min(a[i + 1], b[j + 1])
                    return m1 if (m + n) % 2 else (m1 + m2) / 2
                i += 1
                j -= 1

        if len(a) < len(b):
            return func(a, b)
        else:
            return func(b, a)


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findMedianSortedArrays(nums1, nums2)
    print("\noutput:", serialize(ans, "double"))
