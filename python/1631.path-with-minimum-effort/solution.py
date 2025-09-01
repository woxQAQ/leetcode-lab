# Created by woxQAQ at 2025/09/01 19:12
# leetgo: 1.4.13
# https://leetcode.cn/problems/path-with-minimum-effort/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        l, r = -1, 10**6
        dd = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(mid):
            visited = [[False] * len(heights[0]) for _ in range(len(heights))]

            def dfs(x, y):
                if x == len(heights) - 1 and y == len(heights[0]) - 1:
                    return True
                visited[x][y] = True
                for dx, dy in dd:
                    _x, _y = x + dx, y + dy
                    if (
                        0 <= _x < len(heights)
                        and 0 <= _y < len(heights[0])
                        and not visited[_x][_y]
                        and abs(heights[x][y] - heights[_x][_y]) <= mid
                    ):
                        if dfs(_x, _y):
                            return True
                return False

            return dfs(0, 0)

        while l < r - 1:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m
        return r


# @lc code=end

if __name__ == "__main__":
    heights: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumEffortPath(heights)
    print("\noutput:", serialize(ans, "integer"))
