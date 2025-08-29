# Created by woxQAQ at 2025/08/29 17:18
# leetgo: 1.4.15
# https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-i/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        # if len(s) > 2 * k:
        #     return 0
        l = ans = 0
        cnt = [0, 0]
        # win = r-l+1
        # cnt1 <= k, cnt0= win-cnt1 <=k
        # win-k <= cnt1 <= k
        for r, ch in enumerate(s):
            cnt[ord(ch) - ord("0")] += 1
            while cnt[0] > k and cnt[1] > k:
                cnt[ord(s[l]) - ord("0")] -= 1
                l += 1
            ans += r - l + 1
        return ans


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().countKConstraintSubstrings(s, k)
    print("\noutput:", serialize(ans, "integer"))
