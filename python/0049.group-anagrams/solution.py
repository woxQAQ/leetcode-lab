# Created by woxQAQ at 2026/03/11 17:45
# leetgo: 1.4.16
# https://leetcode.cn/problems/group-anagrams/
from collections import defaultdict

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            m[sorted_s].append(s)
        return list(m.values())
        

# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().groupAnagrams(strs)
    print("\noutput:", serialize(ans, "string[][]"))
