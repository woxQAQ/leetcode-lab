# Created by woxQAQ at 2025/09/04 13:58
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimum-moves-to-convert-string/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimumMoves(self, s: str) -> int:
        ss = list(s)
        ans = 0
        l = 0

        while l < len(ss):
            if ss[l] == "X":
                ans += 1
                l += 3
            else:
                l += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minimumMoves(s)
    print("\noutput:", serialize(ans, "integer"))
