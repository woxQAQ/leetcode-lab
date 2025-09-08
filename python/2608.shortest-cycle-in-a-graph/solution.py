# Created by woxQAQ at 2025/09/08 11:34
# leetgo: 1.4.15
# https://leetcode.cn/problems/shortest-cycle-in-a-graph/

from collections import deque
from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list for the graph
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(start_node):
            """BFS to find the shortest cycle starting from start_node"""
            shortest_cycle = float("inf")
            distances = [-1] * n  # Distance from start_node to each node
            distances[start_node] = 0
            queue = deque([(start_node, -1)])  # (current_node, parent_node)

            while queue:
                current_node, parent_node = queue.popleft()
                for neighbor in graph[current_node]:
                    if distances[neighbor] == -1:  # Not visited yet
                        distances[neighbor] = distances[current_node] + 1
                        queue.append((neighbor, current_node))
                    elif neighbor != parent_node:  # Found a cycle
                        # Cycle length = distance from start to current + distance from start to neighbor + 1
                        cycle_length = distances[current_node] + distances[neighbor] + 1
                        shortest_cycle = min(shortest_cycle, cycle_length)
            return shortest_cycle

        # Find the shortest cycle by starting BFS from each node
        result = min(bfs(i) for i in range(n))
        return result if result != float("inf") else -1


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findShortestCycle(n, edges)
    print("\noutput:", serialize(ans, "integer"))
