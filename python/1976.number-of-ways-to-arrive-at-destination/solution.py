# Created by woxQAQ at 2025/09/08 17:25
# leetgo: 1.4.15
# https://leetcode.cn/problems/number-of-ways-to-arrive-at-destination/

import heapq
from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        g = [[] for _ in range(n)]
        for u, v, w in roads:
            g[u].append((v, w))
            g[v].append((u, w))

        vis = [inf] * n
        vis[0] = 0
        h = [(0, 0)]
        dp = [0] * n
        dp[0] = 1
        while True:
            d, i = heapq.heappop(h)
            if i == n - 1:
                return dp[-1]
            if d > vis[i]:
                continue
            for j, w in g[i]:
                if d + w < vis[j]:
                    vis[j] = d + w
                    heapq.heappush(h, (d + w, j))
                    dp[j] = dp[i]
                elif d + w == vis[j]:
                    dp[j] = (dp[j] + dp[i]) % MOD


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    roads: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countPaths(n, roads)
    print("\noutput:", serialize(ans, "integer"))
