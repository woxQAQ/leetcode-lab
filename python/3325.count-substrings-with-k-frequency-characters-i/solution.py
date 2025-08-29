# Created by woxQAQ at 2025/08/29 18:26
# leetgo: 1.4.15
# https://leetcode.cn/problems/count-substrings-with-k-frequency-characters-i/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        ans = l = 0
        cnt = [0] * 26
        for r, x in enumerate(s):
            cnt[ord(x) - ord("a")] += 1
            while cnt[ord(x) - ord("a")] == k:
                cnt[ord(s[l]) - ord("a")] -= 1
                l += 1
            ans += l
        return ans


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numberOfSubstrings(s, k)
    print("\noutput:", serialize(ans, "integer"))
