# Created by woxQAQ at 2025/09/20 23:47
# leetgo: 1.4.15
# https://leetcode.cn/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

from functools import cache
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = 0

        def dfs(i, st):
            if len(st) != len(set(st)):
                return
            nonlocal res
            res = max(res, len(st))
            if i == len(arr):
                return
            dfs(i + 1, st)
            dfs(i + 1, st + arr[i])

        dfs(0, "")
        return res


# @lc code=end

if __name__ == "__main__":
    arr: List[str] = deserialize("List[str]", read_line())
    ans = Solution().maxLength(arr)
    print("\noutput:", serialize(ans, "integer"))
