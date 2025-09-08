# Created by woxQAQ at 2025/09/08 15:57
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-time-to-visit-disappearing-nodes/

from heapq import heappop, heappush
from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimumTime(
        self, n: int, edges: List[List[int]], disappear: List[int]
    ) -> List[int]:
        # 求每个节点的最短路径 dis
        # if dis[i] + edges[i][j] > disappear[j]: 则 i-j 无法到达
        g = [[] for _ in range(n)]
        for u, v, wt in edges:
            g[u].append((v, wt))
            g[v].append((u, wt))

        dist = [inf] * n
        dist[0] = 0
        h = [(0, 0)]
        while h:
            dx, x = heappop(h)
            if dx > dist[x]:
                continue
            for y, wt in g[x]:
                if dx + wt >= disappear[y]:
                    continue
                nd = dx + wt
                if nd < dist[y]:
                    dist[y] = nd
                    heappush(h, (nd, y))
        return [d if d != inf else -1 for d in dist]


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    disappear: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumTime(n, edges, disappear)
    print("\noutput:", serialize(ans, "integer[]"))
