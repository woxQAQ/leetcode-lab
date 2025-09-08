# Created by woxQAQ at 2025/09/08 17:50
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-edges-in-shortest-paths/

from math import inf
from typing import *
from leetgo_py import *
from heapq import *

# @lc code=begin


class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        g = [[] for _ in range(n)]
        for i, (u, v, w) in enumerate(edges):
            g[u].append((v, w, i))
            g[v].append((u, w, i))

        ans = [False] * len(edges)
        dis = [inf] * n
        dis[0] = 0
        h = [(0, 0)]

        while h:
            d, u = heappop(h)
            if d > dis[u]:
                continue
            for v, w, _ in g[u]:
                nd = dis[u] + w
                if nd < dis[v]:
                    dis[v] = nd
                    heappush(h, (nd, v))

        if dis[-1] == inf:
            return ans
        vis = [False] * n

        def dfs(i):
            vis[i] = True
            for x, w, y in g[i]:
                if dis[x] + w != dis[i]:
                    continue
                ans[y] = True
                if not vis[x]:
                    dfs(x)

        dfs(n - 1)
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findAnswer(n, edges)
    print("\noutput:", serialize(ans, "boolean[]"))
