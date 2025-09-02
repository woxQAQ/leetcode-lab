# Created by woxQAQ at 2025/09/01 20:05
# leetgo: 1.4.13
# https://leetcode.cn/problems/swim-in-rising-water/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        l, r = -1, n * n

        def check(mid):
            if grid[0][0] > mid:
                return False
            visited = set()
            visited.add((0, 0))
            q = Deque([(0, 0)])
            while q:
                x, y = q.popleft()
                if x == y == n - 1:
                    return True
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < n
                        and 0 <= ny < n
                        and grid[nx][ny] <= mid
                        and (nx, ny) not in visited
                    ):
                        visited.add((nx, ny))
                        q.append((nx, ny))

        while l < r - 1:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m
        return r


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().swimInWater(grid)
    print("\noutput:", serialize(ans, "integer"))
