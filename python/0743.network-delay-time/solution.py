# Created by woxQAQ at 2025/09/08 14:56
# leetgo: 1.4.15
# https://leetcode.cn/problems/network-delay-time/

from math import inf
from typing import *
from leetgo_py import *
import heapq

# @lc code=begin


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[] for _ in range(n)]
        for x, y, wt in times:
            g[x - 1].append((y - 1, wt))

        def dijstra(graph: list[list[tuple[int, int]]], start: int):
            dis = [inf] * n
            dis[start] = 0
            h = [(0, start)]
            while h:
                dis_x, x = heapq.heappop(h)
                if dis_x > dis[x]:
                    continue
                for y, wt in graph[x]:
                    new_dis = dis[x] + wt
                    if dis[y] > new_dis:
                        dis[y] = new_dis
                        heapq.heappush(h, (new_dis, y))
            return dis

        dis = dijstra(g, k - 1)
        ans = max(dis)
        return ans if ans < inf else -1


# @lc code=end

if __name__ == "__main__":
    times: List[List[int]] = deserialize("List[List[int]]", read_line())
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().networkDelayTime(times, n, k)
    print("\noutput:", serialize(ans, "integer"))
