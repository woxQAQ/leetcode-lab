# Created by woxQAQ at 2025/09/07 14:51
# leetgo: 1.4.15
# https://leetcode.cn/problems/detonate-the-maximum-bombs/

from collections import defaultdict
import enum
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        g = defaultdict(list)
        for i, (x1, y1, r1) in enumerate(bombs):
            for j, (x2, y2, r2) in enumerate(bombs):
                if i != j and (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r1**2:
                    g[i].append(j)

        def dfs(i):
            visited[i] = True
            nonlocal count
            count += 1
            for j in g[i]:
                if not visited[j]:
                    dfs(j)

        ans = 0
        for i in range(n):
            visited = [False] * n
            count = 0
            dfs(i)
            ans = max(ans, count)
        return ans


# @lc code=end

if __name__ == "__main__":
    bombs: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maximumDetonation(bombs)
    print("\noutput:", serialize(ans, "integer"))
