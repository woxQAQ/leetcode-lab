# Created by woxQAQ at 2025/08/25 15:43
# leetgo: 1.4.15
# https://leetcode.cn/problems/check-if-there-is-a-valid-parentheses-string-path/

"""
2267. 检查是否有合法括号字符串路径 (Hard)
一个括号字符串是一个 **非空** 且只包含 `'('` 和 `')'` 的字符串。如果下面 **任意** 条件为 **真** ，那
么这个括号字符串就是 **合法的** 。

- 字符串是 `()` 。
- 字符串可以表示为 `AB`（ `A` 连接 `B`）， `A` 和 `B` 都是合法括号序列。
- 字符串可以表示为 `(A)` ，其中 `A` 是合法括号序列。

给你一个 `m x n` 的括号网格图矩阵 `grid` 。网格图中一个 **合法括号路径** 是满足以下所有条件的一条路
径：

- 路径开始于左上角格子 `(0, 0)` 。
- 路径结束于右下角格子 `(m - 1, n - 1)` 。
- 路径每次只会向 **下** 或者向 **右** 移动。
- 路径经过的格子组成的括号字符串是 **合法** 的。

如果网格图中存在一条 **合法括号路径** ，请返回 `true` ，否则返回 `false` 。

**示例 1：**

![](https://assets.leetcode.com/uploads/2022/03/15/example1drawio.png)

```
输入：grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
输出：true
解释：上图展示了两条路径，它们都是合法括号字符串路径。
第一条路径得到的合法字符串是 "()(())" 。
第二条路径得到的合法字符串是 "((()))" 。
注意可能有其他的合法括号字符串路径。
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2022/03/15/example2drawio.png)

```
输入：grid = [[")",")"],["(","("]]
输出：false
解释：两条可行路径分别得到 "))(" 和 ")((" 。由于它们都不是合法括号字符串，我们返回 false 。
```

**提示：**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `grid[i][j]` 要么是 `'('` ，要么是 `')'` 。

"""

from functools import cache
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        if (m + n) % 2 == 0 or grid[0][0] == ")" or grid[n - 1][m - 1] == "(":
            return False

        @cache
        def dfs(i, j, c):
            if c > (m + n - 1) - (i + j):
                return False
            if i == n - 1 and j == m - 1:
                return c == 1
            c += 1 if grid[i][j] == "(" else -1
            return (c >= 0) and (
                i < n - 1 and dfs(i + 1, j, c) or j < m - 1 and dfs(i, j + 1, c)
            )

        return dfs(0, 0, 0)


# @lc code=end

if __name__ == "__main__":
    grid: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().hasValidPath(grid)
    print("\noutput:", serialize(ans, "boolean"))
