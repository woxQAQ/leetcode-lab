# Created by woxQAQ at 2025/09/02 07:45
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimize-the-maximum-edge-weight-of-graph/

from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        if len(edges) < n - 1:
            return -1
        max_e = max(edge[2] for edge in edges)
        l, r = -1, max_e + 1
        vis = [0] * n
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[y].append((x, w))

        def check(mid):
            def dfs(i):
                vis[i] = mid
                cnt = 1
                for x, w in g[i]:
                    if vis[x] != mid and w <= mid:
                        cnt += dfs(x)
                return cnt

            return dfs(0) == n

        res = inf
        while l < r - 1:
            mid = (l + r) // 2
            if check(mid):
                r = mid
                res = r
            else:
                l = mid
        return res if res != inf else -1


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    threshold: int = deserialize("int", read_line())
    ans = Solution().minMaxWeight(n, edges, threshold)
    print("\noutput:", serialize(ans, "integer"))
