# Created by woxQAQ at 2026/03/12 00:34
# leetgo: 1.4.16
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/
from collections import defaultdict

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        l = 0
        ans = 0
        for r, ch in enumerate(s):
            window[ch] +=1
            while window[ch] > 1:
                window[s[l]]-=1
                l+=1
            # ans = max(ans,r-l+1)
            ans=max(ans,r-l+1)
        return ans
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().lengthOfLongestSubstring(s)
    print("\noutput:", serialize(ans, "integer"))
