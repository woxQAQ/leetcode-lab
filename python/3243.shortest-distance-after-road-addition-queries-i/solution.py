# Created by woxQAQ at 2025/09/07 19:13
# leetgo: 1.4.15
# https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-i/

from collections import deque
from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        g = [[] for _ in range(n)]
        for i in range(n - 1):
            g[i].append(i + 1)

        def bfs():
            dis = [-1] * n
            dis[0] = 0
            q = deque([0])
            while q:
                x = q.popleft()
                for y in g[x]:
                    if dis[y] == -1:
                        dis[y] = dis[x] + 1
                        q.append(y)
            return dis

        ans = []
        for q in queries:
            g[q[0]].append(q[1])
            dis = bfs()
            ans.append(dis[n - 1])
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().shortestDistanceAfterQueries(n, queries)
    print("\noutput:", serialize(ans, "integer[]"))
