# Created by woxQAQ at 2025/08/29 15:58
# leetgo: 1.4.15
# https://leetcode.cn/problems/smallest-range-covering-elements-from-k-lists/

from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        """ """
        pairs = sorted((p, i) for (i, arr) in enumerate(nums) for p in arr)
        ansl, ansr = -inf, inf
        empty = len(nums)
        cnt = [0] * empty
        left = 0
        for r_val, i in pairs:
            if cnt[i] == 0:
                empty -= 1
            cnt[i] += 1
            while empty == 0:
                l_val, i = pairs[left]
                if r_val - l_val < ansr - ansl:
                    ansl, ansr = l_val, r_val
                cnt[i] -= 1
                if cnt[i] == 0:
                    empty += 1
                left += 1

        return [ansl, ansr]


# @lc code=end

if __name__ == "__main__":
    nums: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().smallestRange(nums)
    print("\noutput:", serialize(ans, "integer[]"))
