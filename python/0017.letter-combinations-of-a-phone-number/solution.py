# Created by woxQAQ at 2025/09/19 17:07
# leetgo: 1.4.15
# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/

from typing import *
from leetgo_py import *

# @lc code=begin
#
digit_to_alpha = [
    "",
    "",
    "abc",
    "def",
    "ghi",
    "jkl",
    "mno",
    "pqrs",
    "tuv",
    "wxyz",
]


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        ans = []
        path = [""] * n

        def dfs(i):
            if i == n:
                ans.append("".join(path))
                return
            for c in digit_to_alpha[int(digits[i])]:
                path[i] = c
                dfs(i + 1)

        dfs(0)
        return ans


# @lc code=end

if __name__ == "__main__":
    digits: str = deserialize("str", read_line())
    ans = Solution().letterCombinations(digits)
    print("\noutput:", serialize(ans, "string[]"))
