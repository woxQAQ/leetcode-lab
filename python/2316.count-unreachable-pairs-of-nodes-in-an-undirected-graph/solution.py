# Created by woxQAQ at 2025/09/07 12:05
# leetgo: 1.4.15
# https://leetcode.cn/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

from collections import defaultdict
import enum
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        vis = [False] * n

        def dfs(i):
            vis[i] = True
            size = 1
            for j in graph[i]:
                if not vis[j]:
                    size += dfs(j)
            return size

        ans = total = 0
        for i in range(n):
            if not vis[i]:
                size = dfs(i)
                ans += size * total
                total += size
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countPairs(n, edges)
    print("\noutput:", serialize(ans, "long"))
