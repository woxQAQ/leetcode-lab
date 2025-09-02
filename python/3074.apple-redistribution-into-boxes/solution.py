# Created by woxQAQ at 2025/09/02 12:14
# leetgo: 1.4.13
# https://leetcode.cn/problems/apple-redistribution-into-boxes/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        s = sum(apple)
        for i, x in enumerate(capacity):
            s -= x
            if s <= 0:
                return i + 1


# @lc code=end

if __name__ == "__main__":
    apple: List[int] = deserialize("List[int]", read_line())
    capacity: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumBoxes(apple, capacity)
    print("\noutput:", serialize(ans, "integer"))
