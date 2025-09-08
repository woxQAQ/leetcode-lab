# Created by woxQAQ at 2025/09/07 14:21
# leetgo: 1.4.15
# https://leetcode.cn/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

from _typeshed import AnyStr_co
from collections import defaultdict
from contextlib import AsyncExitStack
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        for u, v in edges:
            g[v].append(u)

        def dfs(i):
            vis[i] = True
            for j in g[i]:
                if not vis[j]:
                    dfs(j)

        ans = [[] for _ in range(n)]
        for i in range(n):
            vis = [False] * n
            dfs(i)
            vis[i] = False
            ans[i] = [j for j, b in enumerate(vis) if b]

        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().getAncestors(n, edges)
    print("\noutput:", serialize(ans, "integer[][]"))
