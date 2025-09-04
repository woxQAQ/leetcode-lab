# Created by woxQAQ at 2025/09/04 09:46
# leetgo: 1.4.13
# https://leetcode.cn/problems/assign-cookies/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        for cookie in s:
            if cookie < g[ans]:
                continue
            ans += 1
            if ans == len(g):
                break
        return ans


# @lc code=end

if __name__ == "__main__":
    g: List[int] = deserialize("List[int]", read_line())
    s: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findContentChildren(g, s)
    print("\noutput:", serialize(ans, "integer"))
