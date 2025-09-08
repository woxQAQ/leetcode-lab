# Created by woxQAQ at 2025/09/07 10:28
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-if-path-exists-in-graph/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node):
            if node == destination:
                return True
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor] and dfs(neighbor):
                    return True
            return False

        return dfs(source)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    source: int = deserialize("int", read_line())
    destination: int = deserialize("int", read_line())
    ans = Solution().validPath(n, edges, source, destination)
    print("\noutput:", serialize(ans, "boolean"))
