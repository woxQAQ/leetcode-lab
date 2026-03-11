# Created by woxQAQ at 2026/03/12 00:45
# leetgo: 1.4.16
# https://leetcode.cn/problems/find-all-anagrams-in-a-string/
from collections import defaultdict

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p)
        l = 0
        ans = []
        for r,c in enumerate(s):
            counter[c] -= 1
            while counter[c] < 0:
                counter[s[l]] +=1
                l+=1
            if r-l+1 == len(p):
                ans.append(l)
        return ans
                

        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    p: str = deserialize("str", read_line())
    ans = Solution().findAnagrams(s, p)
    print("\noutput:", serialize(ans, "integer[]"))
