# Created by woxQAQ at 2026/03/12 02:58
# leetgo: 1.4.16
# https://leetcode.cn/problems/minimum-window-substring/
from collections import defaultdict

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        for char in t:
            need[char] += 1

        left = 0
        min_left, min_right = -1, len(s)
        matches = 0
        required = len(need)

        for right, char in enumerate(s):
            if char in need:
                need[char] -= 1
                if need[char] == 0:
                    matches += 1

                while matches == required:
                    if right - left < min_right - min_left:
                        min_left = left
                        min_right = right

                    left_char = s[left]
                    if left_char in need:
                        if need[left_char] == 0:
                            matches -= 1
                        need[left_char] += 1
                    left += 1

        return "" if min_left < 0 else s[min_left:min_right + 1]

        
                

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().minWindow(s, t)
    print("\noutput:", serialize(ans, "string"))
