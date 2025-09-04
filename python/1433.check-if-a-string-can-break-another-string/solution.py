# Created by woxQAQ at 2025/09/04 10:23
# leetgo: 1.4.13
# https://leetcode.cn/problems/check-if-a-string-can-break-another-string/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        # 'a' 'b' 'c'
        # 'a' 'x' 'y'
        a = sorted(s1)
        b = sorted(s2)
        return all(x <= y for x, y in zip(a, b)) or all(x >= y for x, y in zip(a, b))


# @lc code=end

if __name__ == "__main__":
    s1: str = deserialize("str", read_line())
    s2: str = deserialize("str", read_line())
    ans = Solution().checkIfCanBreak(s1, s2)
    print("\noutput:", serialize(ans, "boolean"))
