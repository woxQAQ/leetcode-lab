# Created by woxQAQ at 2025/08/25 19:46
# leetgo: 1.4.15
# https://leetcode.cn/problems/profitable-schemes/

"""
879. 盈利计划 (Hard)
集团里有 `n` 名员工，他们可以完成各种各样的工作创造利润。

第 `i` 种工作会产生 `profit[i]` 的利润，它要求 `group[i]` 名成员共同参与。如果成员参与了其中一项工作
，就不能参与另一项工作。

工作的任何至少产生 `minProfit` 利润的子集称为 **盈利计划** 。并且工作的成员总数最多为 `n` 。

有多少种计划可以选择？因为答案很大，所以 **返回结果模** `10^9 + 7` **的值**。

**示例 1：**

```
输入：n = 5, minProfit = 3, group = [2,2], profit = [2,3]
输出：2
解释：至少产生 3 的利润，该集团可以完成工作 0 和工作 1 ，或仅完成工作 1 。
总的来说，有两种计划。
```

**示例 2：**

```
输入：n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
输出：7
解释：至少产生 5 的利润，只要完成其中一种工作就行，所以该集团可以完成任何工作。
有 7 种可能的计划：(0)，(1)，(2)，(0,1)，(0,2)，(1,2)，以及 (0,1,2) 。
```

**提示：**

- `1 <= n <= 100`
- `0 <= minProfit <= 100`
- `1 <= group.length <= 100`
- `1 <= group[i] <= 100`
- `profit.length == group.length`
- `0 <= profit[i] <= 100`

"""

from functools import cache
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def profitableSchemes(
        self, n: int, minProfit: int, group: List[int], profit: List[int]
    ) -> int:
        """
        dfs(i,j,k): 剩余员工 i 的条件下，在项目 0...j中可以完成最低利润 k 的方案数
        n = 5, minProfit = 3, group = [2,2], profit = [2,3]
        profit[j] > k
            1. i < group[j]: 不能选
            2. i >= group[j]: 可以选，
                选则为终点
                不选，则继续递归 dfs(i, j-1, k)
        profit[j] <= k
            1. i < group[j]: 不能选
            2. i >= group[j]: 可以选,
                选则继续递归 dfs(i-group[j], j-1, k-profit[j])
                不选则递归 dfs(i,j-1,k)
        """
        MOD = 10**9 + 7

        @cache
        def dfs(i, j, k):
            if j < 0:
                return int(k <= 0)
            if i < group[j]:
                return dfs(i, j - 1, k)
            return (
                dfs(i, j - 1, k) + dfs(i - group[j], j - 1, max(0, k - profit[j]))
            ) % MOD

        return dfs(n, len(group) - 1, minProfit) % MOD


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    minProfit: int = deserialize("int", read_line())
    group: List[int] = deserialize("List[int]", read_line())
    profit: List[int] = deserialize("List[int]", read_line())
    ans = Solution().profitableSchemes(n, minProfit, group, profit)
    print("\noutput:", serialize(ans, "integer"))
