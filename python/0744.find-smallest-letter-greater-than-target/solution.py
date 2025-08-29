# Created by woxQAQ at 2025/08/29 21:11
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-smallest-letter-greater-than-target/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
        l = -1
        r = len(letters)
        while l < r - 1:
            mid = l + (r - l) // 2
            if letters[mid] < chr(ord(target) + 1):
                l = mid
            else:
                r = mid
        return letters[r]


# @lc code=end

if __name__ == "__main__":
    letters: List[str] = deserialize("List[str]", read_line())
    target: str = deserialize("str", read_line())
    ans = Solution().nextGreatestLetter(letters, target)
    print("\noutput:", serialize(ans, "character"))
