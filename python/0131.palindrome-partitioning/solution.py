# Created by woxQAQ at 2025/09/21 01:23
# leetgo: 1.4.15
# https://leetcode.cn/problems/palindrome-partitioning/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []

        def dfs(i):
            if i == len(s):
                ans.append(path[:])
                return
            for j in range(i, len(s)):
                if s[i : j + 1] == s[i : j + 1][::-1]:
                    path.append(s[i : j + 1])
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return ans


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().partition(s)
    print("\noutput:", serialize(ans, "string[][]"))
