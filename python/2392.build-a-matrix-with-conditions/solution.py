# Created by woxQAQ at 2025/09/08 12:43
# leetgo: 1.4.15
# https://leetcode.cn/problems/build-a-matrix-with-conditions/

from collections import deque
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:
        def topo_sort(edges: list[list[int]]) -> list[int] | None:
            ans = []
            g = [[] for _ in range(k)]
            indeg = [0] * k

            for u, v in edges:
                g[u - 1].append(v - 1)
                indeg[v - 1] += 1

            q = deque(i for i, d in enumerate(indeg) if d == 0)
            while q:
                u = q.popleft()
                ans.append(u)
                for v in g[u]:
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        q.append(v)
            return ans if len(ans) == k else None

        row, col = topo_sort(rowConditions), topo_sort(colConditions)
        if row is None or col is None:
            return []

        ans = [[0] * k for _ in range(k)]
        pos = {x: i for i, x in enumerate(col)}
        for i, x in enumerate(row):
            ans[i][pos[x]] = x + 1
        return ans


# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    rowConditions: List[List[int]] = deserialize("List[List[int]]", read_line())
    colConditions: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().buildMatrix(k, rowConditions, colConditions)
    print("\noutput:", serialize(ans, "integer[][]"))
