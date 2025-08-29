# Created by woxQAQ at 2025/08/29 18:16
# leetgo: 1.4.15
# https://leetcode.cn/problems/number-of-substrings-containing-all-three-characters/

from collections import defaultdict
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = defaultdict(int)
        ans = l = 0
        for r, x in enumerate(s):
            cnt[x] += 1
            while len(cnt) == 3:
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0:
                    del cnt[s[l]]
                l += 1
            ans += l
        return ans


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().numberOfSubstrings(s)
    print("\noutput:", serialize(ans, "integer"))
