# Created by woxQAQ at 2025/08/26 00:21
# leetgo: 1.4.15
# https://leetcode.cn/problems/perfect-squares/

"""
279. 完全平方数 (Medium)
给你一个整数 `n` ，返回 和为 `n` 的完全平方数的最少数量 。

**完全平方数** 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如， `1`
、 `4`、 `9` 和 `16` 都是完全平方数，而 `3` 和 `11` 不是。

**示例 1：**

```
输入：n = 12
输出：3
解释：12 = 4 + 4 + 4
```

**示例 2：**

```
输入：n = 13
输出：2
解释：13 = 4 + 9
```

**提示：**

- `1 <= n <= 10⁴`

"""

from functools import cache
from typing import *
from leetgo_py import *
from math import inf, isqrt


# @lc code=begin
@cache
def dfs(i, c):
    if i == 0:
        return inf if c else 0

    if c < i * i:
        return dfs(i - 1, c)
    return min(dfs(i - 1, c), dfs(i, c - i * i) + 1)


class Solution:
    def numSquares(self, n: int) -> int:
        return dfs(isqrt(n), n)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().numSquares(n)
    print("\noutput:", serialize(ans, "integer"))
