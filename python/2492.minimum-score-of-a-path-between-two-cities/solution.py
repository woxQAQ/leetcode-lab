# Created by woxQAQ at 2025/09/07 12:46
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-score-of-a-path-between-two-cities/

from collections import defaultdict
from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        vis = [False] * (n + 1)
        ans = inf

        def dfs(i):
            vis[i] = True
            nonlocal ans
            for j, w in graph[i]:
                ans = min(ans, w)
                if not vis[j]:
                    dfs(j)

        dfs(1)

        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    roads: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minScore(n, roads)
    print("\noutput:", serialize(ans, "integer"))
