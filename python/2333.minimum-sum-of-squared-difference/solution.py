# Created by woxQAQ at 2025/09/03 20:04
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimum-sum-of-squared-difference/

from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minSumSquareDiff(
        self, nums1: List[int], nums2: List[int], k1: int, k2: int
    ) -> int:
        # [1,8,15,17]
        #
        # 可以证明，对于d1>d2
        # d1^2 - (d1-1)^2= 2d1-1 > 2d2_1
        # 即对大的数字进行 '-' 操作所能减少的平方和最大
        # 因此我们优先对 diff 值较大的下标进行操作
        #
        # 由于我们对数字可以加或者减，
        # 对 d1 进行加等价于对 d2 进行减
        # 因此我们只需要对 diff 进行操作即可

        # diff = sorted([abs(a - b) for a, b in zip(nums1, nums2)], reverse=True)
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        ans = sum(d * d for d in diff)

        ops = k1 + k2

        if sum(diff) < ops:
            return 0

        diff.sort(reverse=True)
        diff += [0]
        for i, v in enumerate(diff):
            ans -= v * v
            j = i + 1
            c = j * (v - diff[j])
            if c < ops:
                ops -= c
                continue
            v -= ops // j
            return ans + (v - 1) * (v - 1) * (ops % j) + (j - ops % j) * v * v


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    k1: int = deserialize("int", read_line())
    k2: int = deserialize("int", read_line())
    ans = Solution().minSumSquareDiff(nums1, nums2, k1, k2)
    print("\noutput:", serialize(ans, "long"))
