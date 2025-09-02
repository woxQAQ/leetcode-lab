# Created by woxQAQ at 2025/09/02 12:22
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimum-deletions-for-at-most-k-distinct-characters/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        cnt = sorted(Counter(s).values())
        return sum(cnt[:-k])


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minDeletion(s, k)
    print("\noutput:", serialize(ans, "integer"))
