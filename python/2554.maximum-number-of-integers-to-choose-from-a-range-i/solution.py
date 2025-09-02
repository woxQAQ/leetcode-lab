# Created by woxQAQ at 2025/09/02 14:44
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximum-number-of-integers-to-choose-from-a-range-i/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban = set(banned)
        res = 0
        s = 0
        for i in range(1, n + 1):
            if i not in ban and s + i <= maxSum:
                res += 1
                s += i
        return res


# @lc code=end

if __name__ == "__main__":
    banned: List[int] = deserialize("List[int]", read_line())
    n: int = deserialize("int", read_line())
    maxSum: int = deserialize("int", read_line())
    ans = Solution().maxCount(banned, n, maxSum)
    print("\noutput:", serialize(ans, "integer"))
