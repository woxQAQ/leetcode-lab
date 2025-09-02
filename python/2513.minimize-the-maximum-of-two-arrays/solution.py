# Created by woxQAQ at 2025/09/02 09:01
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimize-the-maximum-of-two-arrays/

from copyreg import dispatch_table
import math
from os import dup2
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimizeSet(
        self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int
    ) -> int:
        l, r = -1, (uniqueCnt1 + uniqueCnt2) * 2
        lcm = math.lcm(divisor1, divisor2)

        def check(mid):
            left1 = max(uniqueCnt1 - mid // divisor2 + mid // lcm, 0)
            left2 = max(uniqueCnt2 - mid // divisor1 + mid // lcm, 0)
            common = mid - mid // divisor1 - mid // divisor2 + mid // lcm
            return common >= left1 + left2

        while l < r - 1:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m
        return r


# @lc code=end

if __name__ == "__main__":
    divisor1: int = deserialize("int", read_line())
    divisor2: int = deserialize("int", read_line())
    uniqueCnt1: int = deserialize("int", read_line())
    uniqueCnt2: int = deserialize("int", read_line())
    ans = Solution().minimizeSet(divisor1, divisor2, uniqueCnt1, uniqueCnt2)
    print("\noutput:", serialize(ans, "integer"))
