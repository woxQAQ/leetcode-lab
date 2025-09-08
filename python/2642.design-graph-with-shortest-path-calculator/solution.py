# Created by woxQAQ at 2025/09/08 16:19
# leetgo: 1.4.15
# https://leetcode.cn/problems/design-graph-with-shortest-path-calculator/

from heapq import heappop, heappush
from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.g = [[] for _ in range(n)]
        self.n = n
        for u, v, wt in edges:
            self.g[u].append((v, wt))

    def addEdge(self, edge: List[int]) -> None:
        self.g[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        n = self.n
        vis = [inf] * n
        vis[node1] = 0
        h = [(0, node1)]

        while h:
            dis_x, x = heappop(h)
            if dis_x > vis[x]:
                continue
            if x == node2:
                return dis_x
            for y, wt in self.g[x]:
                if dis_x + wt < vis[y]:
                    vis[y] = dis_x + wt
                    heappush(h, (vis[y], y))
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    n: int = deserialize("int", constructor_params[0])
    edges: List[List[int]] = deserialize(
        "List[List[int]]", constructor_params[1]
    )
    obj = Graph(n, edges)

    for i in range(1, len(ops)):
        match ops[i]:
            case "addEdge":
                method_params = split_array(params[i])
                edge: List[int] = deserialize("List[int]", method_params[0])
                obj.addEdge(edge)
                output.append("null")
            case "shortestPath":
                method_params = split_array(params[i])
                node1: int = deserialize("int", method_params[0])
                node2: int = deserialize("int", method_params[1])
                ans = serialize(obj.shortestPath(node1, node2))
                output.append(ans)

    print("\noutput:", join_array(output))
