# Created by woxQAQ at 2025/09/07 13:56
# leetgo: 1.4.15
# https://leetcode.cn/problems/count-the-number-of-complete-components/

from collections import defaultdict
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        vis = [False] * n

        def dfs(i):
            vis[i] = True
            nonlocal v, e
            v += 1
            e += len(g[i])
            for j in g[i]:
                if not vis[j]:
                    dfs(j)

        ans = 0
        for i in range(n):
            if not vis[i]:
                v = e = 0
                dfs(i)
                if v * (v - 1) == e:
                    ans += 1

        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countCompleteComponents(n, edges)
    print("\noutput:", serialize(ans, "integer"))
