# Created by woxQAQ at 2025/09/08 15:15
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-minimum-time-to-reach-last-room-i/

from heapq import heappop, heappush
from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        dis = [[inf] * m for _ in range(n)]
        dis[0][0] = 0
        h = [(0, 0, 0)]
        while True:
            d, i, j = heappop(h)
            if i == n - 1 and j == m - 1:
                return d
            if d > dis[i][j]:
                continue
            time = 1
            for x, y in (i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1):
                if 0 <= x < n and 0 <= y < m:
                    nd = max(d, moveTime[x][y]) + time
                    if nd < dis[x][y]:
                        dis[x][y] = nd
                        heappush(h, (nd, x, y))


# @lc code=end

if __name__ == "__main__":
    moveTime: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minTimeToReach(moveTime)
    print("\noutput:", serialize(ans, "integer"))
