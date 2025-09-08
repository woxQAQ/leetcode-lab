# Created by woxQAQ at 2025/09/08 17:15
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-cost-path-with-edge-reversals/

import heapq
from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        inedges = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, 2 * w))
        dist = [inf] * n
        dist[0] = 0

        pq = [(0, 0)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            if u == n - 1:
                return d
            for v, w in g[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        return dist[n - 1] if dist[n - 1] != inf else -1


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minCost(n, edges)
    print("\noutput:", serialize(ans, "integer"))
