# Created by woxQAQ at 2025/08/31 14:18
# leetgo: 1.4.13
# https://leetcode.cn/problems/h-index-ii/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        r = len(citations) + 1
        while l < r - 1:
            m = (l + r) // 2
            if citations[-m] >= m:
                l = m
            else:
                r = m
        return l


# @lc code=end

if __name__ == "__main__":
    citations: List[int] = deserialize("List[int]", read_line())
    ans = Solution().hIndex(citations)
    print("\noutput:", serialize(ans, "integer"))
