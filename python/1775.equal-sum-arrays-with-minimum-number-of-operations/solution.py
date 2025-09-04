# Created by woxQAQ at 2025/09/03 15:54
# leetgo: 1.4.13
# https://leetcode.cn/problems/equal-sum-arrays-with-minimum-number-of-operations/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        d = s2 - s1

        def func(n1, n2):
            nonlocal d
            ans = 0
            cnt = Counter(6 - x for x in n1) + Counter(x - 1 for x in n2)
            for i in range(5, 0, -1):
                if i * cnt[i] >= d:
                    return ans + (d + i - 1) // i
                ans += cnt[i]
                d -= i * cnt[i]
            return -1

        if s1 > s2:
            d = -d
            return func(nums2, nums1)
        else:
            return func(nums1, nums2)


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minOperations(nums1, nums2)
    print("\noutput:", serialize(ans, "integer"))
