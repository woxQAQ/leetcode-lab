# Created by woxQAQ at 2025/09/08 16:34
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-time-to-reach-destination-in-directed-graph/

from heapq import heappop, heappush
from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v, start, end in edges:
            g[u].append((v, start, end))

        vis = [inf] * n
        vis[0] = 0
        h = [(0, 0)]
        while h:
            dis_x, x = heappop(h)
            if vis[x] < dis_x:
                continue

            for y, start, end in g[x]:
                if start <= dis_x <= end:
                    dis_y = dis_x + 1
                elif start > dis_x:
                    dis_y = start + 1
                else:
                    continue
                if dis_y < vis[y]:
                    vis[y] = dis_y
                    heappush(h, (dis_y, y))

        return vis[n - 1] if vis[n - 1] != inf else -1


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minTime(n, edges)
    print("\noutput:", serialize(ans, "integer"))
