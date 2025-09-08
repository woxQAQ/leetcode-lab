# Created by woxQAQ at 2025/09/07 17:30
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-eventual-safe-states/

from collections import deque
import enum
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # g = DefaultDict(list)
        # for i, neighbors in enumerate(graph):
        #     g[i].extend(neighbors)
        # n = len(graph)
        # visited = [0] * n

        # def dfs(i):
        #     if visited[i] > 0:
        #         return visited[i] == 2
        #     visited[i] = 1
        #     for y in g[i]:
        #         if not dfs(y):
        #             return False
        #     visited[i] = 2
        #     return True

        # return [i for i in range(n) if dfs(i)]

        n = len(graph)
        outdeg = [0] * n
        g = [[] for _ in range(n)]
        for i, x in enumerate(graph):
            outdeg[i] += len(x)
            for end in x:
                g[end].append(i)

        q = deque(i for i in range(n) if outdeg[i] == 0)
        ans = []
        while q:
            x = q.popleft()
            ans.append(x)
            for y in g[x]:
                outdeg[y] -= 1
                if outdeg[y] == 0:
                    q.append(y)
        return sorted(ans)


# @lc code=end

if __name__ == "__main__":
    graph: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().eventualSafeNodes(graph)
    print("\noutput:", serialize(ans, "integer[]"))
