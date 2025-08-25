# Created by woxQAQ at 2025/08/25 15:20
# leetgo: 1.4.15
# https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/

"""
329. 矩阵中的最长递增路径 (Hard)
给定一个 `m x n` 整数矩阵 `matrix` ，找出其中 **最长递增路径** 的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你 **不能** 在 **对角线** 方向上移动或移动到 **
边界外**（即不允许环绕）。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/01/05/grid1.jpg)

```
输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
输出：4
解释：最长递增路径为 [1, 2, 6, 9]。
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/01/27/tmp-grid.jpg)

```
输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
输出：4
解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
```

**示例 3：**

```
输入：matrix = [[1]]
输出：1
```

**提示：**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 200`
- `0 <= matrix[i][j] <= 2³¹ - 1`

"""

from functools import cache
from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        搜索所有路径
        """
        dd = (1,0),(0,1),(-1,0),(0,-1)
        @cache
        def dfs(i,j):
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
                return 0
            res = 0
            for dx,dy in dd:
                if 0<=i+dx<len(matrix) and 0<=j+dy<len(matrix[0]) and matrix[i][j]<matrix[i+dx][j+dy]:
                    res = max(res, dfs(i+dx,j+dy))
            return res + 1

        return max(dfs(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])))

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().longestIncreasingPath(matrix)
    print("\noutput:", serialize(ans, "integer"))
