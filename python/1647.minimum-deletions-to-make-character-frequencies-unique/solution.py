# Created by woxQAQ at 2025/09/03 08:01
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimum-deletions-to-make-character-frequencies-unique/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minDeletions(self, s: str) -> int:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord("a")] += 1
        freq.sort(reverse=True)
        ops = 0
        for i in range(1, len(freq)):
            # [2,3,3]
            if not freq[i]:
                continue
            while freq[i] >= freq[i - 1] and freq[i] > 0:
                freq[i] -= 1
                ops += 1
        return ops


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minDeletions(s)
    print("\noutput:", serialize(ans, "integer"))
