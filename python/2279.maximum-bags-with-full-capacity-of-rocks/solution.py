# Created by woxQAQ at 2025/09/02 12:37
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximum-bags-with-full-capacity-of-rocks/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumBags(
        self, capacity: List[int], rocks: List[int], additionalRocks: int
    ) -> int:
        left = sorted(c - r for c, r in zip(capacity, rocks))
        for i, l in enumerate(left):
            if l > additionalRocks:
                return i
            additionalRocks -= l
        return len(left)


# @lc code=end

if __name__ == "__main__":
    capacity: List[int] = deserialize("List[int]", read_line())
    rocks: List[int] = deserialize("List[int]", read_line())
    additionalRocks: int = deserialize("int", read_line())
    ans = Solution().maximumBags(capacity, rocks, additionalRocks)
    print("\noutput:", serialize(ans, "integer"))
