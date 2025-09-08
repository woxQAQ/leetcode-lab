# Created by woxQAQ at 2025/09/07 17:30
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-eventual-safe-states/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        g = DefaultDict(list)
        for i, neighbors in enumerate(graph):
            g[i].extend(neighbors)
        n = len(graph)
        visited = [0] * n

        def dfs(i):
            if visited[i] > 0:
                return visited[i] == 2
            visited[i] = 1
            for y in g[i]:
                if not dfs(y):
                    return False
            visited[i] = 2
            return True

        return [i for i in range(n) if dfs(i)]


# @lc code=end

if __name__ == "__main__":
    graph: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().eventualSafeNodes(graph)
    print("\noutput:", serialize(ans, "integer[]"))
