# Created by woxQAQ at 2025/09/03 06:49
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximize-the-total-height-of-unique-towers/

from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        s = maximumHeight[0]
        for i in range(1, len(maximumHeight)):
            maximumHeight[i] = min(maximumHeight[i], maximumHeight[i - 1] - 1)
            if maximumHeight[i] <= 0:
                return -1
            s += maximumHeight[i]

        return s


# @lc code=end

if __name__ == "__main__":
    maximumHeight: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumTotalSum(maximumHeight)
    print("\noutput:", serialize(ans, "long"))
