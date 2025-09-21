# Created by woxQAQ at 2025/09/21 01:41
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-the-punishment-number-of-an-integer/

from functools import cache
from typing import *
from leetgo_py import *
from math import isqrt

# @lc code=begin


class Solution:
    def punishmentNumber(self, n: int) -> int:
        res = 0

        for i in range(1, n + 1):
            s = str(i * i)

            def check(k, _sum):
                if k == len(s):
                    return _sum == i
                x = 0
                for j in range(k, len(s)):
                    x = x * 10 + int(s[j])
                    if check(j + 1, _sum + x):
                        return True
                return False

            if check(0, 0):
                res += i * i

        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().punishmentNumber(n)
    print("\noutput:", serialize(ans, "integer"))
