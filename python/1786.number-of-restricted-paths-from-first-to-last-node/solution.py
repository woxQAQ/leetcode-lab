# Created by woxQAQ at 2025/09/08 18:09
# leetgo: 1.4.15
# https://leetcode.cn/problems/number-of-restricted-paths-from-first-to-last-node/

import heapq
from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u - 1].append((v - 1, w))
            g[v - 1].append((u - 1, w))

        def dijstra(start):
            dist = [inf] * n
            dist[start] = 0
            pq = [(0, start)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                for v, w in g[u]:
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        heapq.heappush(pq, (dist[v], v))
            return dist

        dist = dijstra(n - 1)

        nodes = sorted(range(n), key=lambda x: dist[x])
        dp = [0] * n
        dp[n - 1] = 1
        for i in nodes:
            if i == n - 1:
                continue
            for j, w in g[i]:
                if dist[i] > dist[j]:
                    dp[i] = (dp[i] + dp[j]) % MOD
        return dp[0]


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countRestrictedPaths(n, edges)
    print("\noutput:", serialize(ans, "integer"))
