# Created by woxQAQ at 2025/09/20 20:52
# leetgo: 1.4.15
# https://leetcode.cn/problems/letter-case-permutation/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        path = [""] * len(s)

        def dfs(i):
            if i == len(s):
                ans.append("".join(path))
                return
            if s[i].isalpha():
                path[i] = s[i]
                dfs(i + 1)
                path[i] = s[i].swapcase()
                dfs(i + 1)
            else:
                path[i] = s[i]
                dfs(i + 1)

        dfs(0)
        return ans


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().letterCasePermutation(s)
    print("\noutput:", serialize(ans, "string[]"))
