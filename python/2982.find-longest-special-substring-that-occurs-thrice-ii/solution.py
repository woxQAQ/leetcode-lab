# Created by woxQAQ at 2025/08/31 15:00
# leetgo: 1.4.13
# https://leetcode.cn/problems/find-longest-special-substring-that-occurs-thrice-ii/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumLength(self, s: str) -> int:
        count = DefaultDict(list)
        tmp = 0
        for i, x in enumerate(s):
            tmp += 1
            if i == len(s) - 1 or x != s[i + 1]:
                count[x].append(tmp)
                tmp = 0
        ans = 0
        for a in count.values():
            a.sort(reverse=True)
            a.extend([0, 0])
            ans = max(ans, a[0] - 2, min(a[0] - 1, a[1]), a[2])
        return ans if ans > 0 else -1


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().maximumLength(s)
    print("\noutput:", serialize(ans, "integer"))
