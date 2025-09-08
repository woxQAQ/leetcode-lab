# Created by woxQAQ at 2025/09/08 17:00
# leetgo: 1.4.15
# https://leetcode.cn/problems/path-with-maximum-probability/

from heapq import heappop, heappush
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        g = [[] for _ in range(n)]
        for (x, y), p in zip(edges, succProb):
            g[x].append((y, p))
            g[y].append((x, p))

        dist = [0.0] * n
        dist[start_node] = 1.0

        # 这里取负号是因为 h 是最小堆，按照距离的负值排序
        # 否则，如果距离相同，会优先选择更小的节点，导致错误结果
        h = [(-dist[start_node], start_node)]

        while h:
            dis_x, x = heappop(h)
            dis_x *= -1
            if dis_x > dist[x]:
                continue
            if x == end_node:
                return dis_x
            for y, p in g[x]:
                if dist[y] < dist[x] * p:
                    dist[y] = dist[x] * p
                    heappush(h, (-dist[y], y))

        return 0


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    succProb: List[float] = deserialize("List[float]", read_line())
    start_node: int = deserialize("int", read_line())
    end_node: int = deserialize("int", read_line())
    ans = Solution().maxProbability(n, edges, succProb, start_node, end_node)
    print("\noutput:", serialize(ans, "double"))
