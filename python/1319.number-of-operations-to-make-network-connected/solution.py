# Created by woxQAQ at 2025/09/07 12:38
# leetgo: 1.4.15
# https://leetcode.cn/problems/number-of-operations-to-make-network-connected/

from collections import defaultdict
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if n - 1 > len(connections):
            return -1
        count = 0
        vis = [False] * n

        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(i):
            vis[i] = True
            for j in graph[i]:
                if not vis[j]:
                    dfs(j)

        for i in range(n):
            if not vis[i]:
                count += 1
                dfs(i)

        return count - 1 if count - 1 <= len(connections) else -1


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    connections: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().makeConnected(n, connections)
    print("\noutput:", serialize(ans, "integer"))
