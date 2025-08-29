# Created by woxQAQ at 2025/08/29 02:44
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-window-substring/

from collections import defaultdict
from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # s= [ADOBEC]ODEBANC, t= ABC
        # cnt_t: Counter({'A': 1, 'B': 1, 'C': 1})
        l = 0
        cnt = defaultdict(int)
        for c in t:
            cnt[c] += 1
        ansl, ansr = -1, len(s)
        # Count how many characters we still need (unique chars in t)
        required = len([k for k, v in cnt.items() if v > 0])
        formed = 0
        for r, c in enumerate(s):
            if c in cnt:
                cnt[c] -= 1
                if cnt[c] == 0:
                    formed += 1
            while formed == required:
                if r - l < ansr - ansl:
                    ansl, ansr = l, r
                x = s[l]
                if x in cnt:
                    if cnt[x] == 0:
                        formed -= 1
                    cnt[x] += 1
                l += 1
        return "" if ansl < 0 else s[ansl : ansr + 1]


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().minWindow(s, t)
    print("\noutput:", serialize(ans, "string"))
