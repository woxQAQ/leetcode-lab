# Created by woxQAQ at 2025/08/25 15:32
# leetgo: 1.4.15
# https://leetcode.cn/problems/number-of-increasing-paths-in-a-grid/

"""
2328. 网格图中递增路径的数目 (Hard)
给你一个 `m x n` 的整数网格图 `grid` ，你可以从一个格子移动到 `4` 个方向相邻的任意一个格子。

请你返回在网格图中从 **任意** 格子出发，达到 **任意** 格子，且路径中的数字是 **严格递增** 的路径数目
。由于答案可能会很大，请将结果对 `10⁹ + 7` **取余** 后返回。

如果两条路径中访问过的格子不是完全相同的，那么它们视为两条不同的路径。

**示例 1：**

![](https://assets.leetcode.com/uploads/2022/05/10/griddrawio-4.png)

```
输入：grid = [[1,1],[3,4]]
输出：8
解释：严格递增路径包括：
- 长度为 1 的路径：[1]，[1]，[3]，[4] 。
- 长度为 2 的路径：[1 -> 3]，[1 -> 4]，[3 -> 4] 。
- 长度为 3 的路径：[1 -> 3 -> 4] 。
路径数目为 4 + 3 + 1 = 8 。
```

**示例 2：**

```
输入：grid = [[1],[2]]
输出：3
解释：严格递增路径包括：
- 长度为 1 的路径：[1]，[2] 。
- 长度为 2 的路径：[1 -> 2] 。
路径数目为 2 + 1 = 3 。
```

**提示：**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 1000`
- `1 <= m * n <= 10⁵`
- `1 <= grid[i][j] <= 10⁵`

"""

from functools import cache
from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        dd=[(0,1),(0,-1),(1,0),(-1,0)]
        m,n=len(grid),len(grid[0])
        @cache
        def dfs(i,j):
            res=0
            for dx,dy in dd:
                if 0<=i+dx<m and 0<=j+dy<n and grid[i][j]<grid[i+dx][j+dy]:
                    res+=dfs(i+dx,j+dy)
            return res+1
        return sum(dfs(i,j) for i in range(m) for j in range(n)) % (10**9 + 7)


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countPaths(grid)
    print("\noutput:", serialize(ans, "integer"))
