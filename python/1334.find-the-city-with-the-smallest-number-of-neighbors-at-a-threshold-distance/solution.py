# Created by woxQAQ at 2025/09/08 19:13
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        dp = [[inf] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0

        for x, y, wt in edges:
            dp[x][y] = min(dp[x][y], wt)
            dp[y][x] = min(dp[y][x], wt)

        for k in range(n):
            for i in range(n):
                if dp[i][k] == inf:
                    continue
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

        min_city = -1
        min_count = inf
        for i in range(n):
            count = sum(1 for j in range(n) if dp[i][j] <= distanceThreshold)
            if count <= min_count:
                min_count = count
                min_city = i

        return min_city


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    distanceThreshold: int = deserialize("int", read_line())
    ans = Solution().findTheCity(n, edges, distanceThreshold)
    print("\noutput:", serialize(ans, "integer"))
