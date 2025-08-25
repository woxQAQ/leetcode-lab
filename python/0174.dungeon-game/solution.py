# Created by woxQAQ at 2025/08/25 02:07
# leetgo: 1.4.15
# https://leetcode.cn/problems/dungeon-game/

"""
174. 地下城游戏 (Hard)
恶魔们抓住了公主并将她关在了地下城 `dungeon` 的 **右下角** 。地下城是由 `m x n` 个房间组成的二维网格
。我们英勇的骑士最初被安置在 **左上角** 的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。

骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。

有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健
康点数）；其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整
数，则表示骑士将增加健康点数）。

为了尽快解救公主，骑士决定每次只 **向右** 或 **向下** 移动一步。

返回确保骑士能够拯救到公主所需的最低初始健康点数。

**注意：** 任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房
间以及公主被监禁的右下角房间。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/13/dungeon-grid-1.jpg)

```
输入：dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
输出：7
解释：如果骑士遵循最佳路径：右 -> 右 -> 下 -> 下 ，则骑士的初始健康点数至少为 7 。
```

**示例 2：**

```
输入：dungeon = [[0]]
输出：1
```

**提示：**

- `m == dungeon.length`
- `n == dungeon[i].length`
- `1 <= m, n <= 200`
- `-1000 <= dungeon[i][j] <= 1000`

"""

from functools import cache
from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
        dfs(i,j) (i,j) 出发到 (n-1,m-1) 所需的最小生命值
        """
        n,m=len(dungeon),len(dungeon[0])
        @cache
        def dfs(i,j):
            if i >= n or j >= m:
                return inf
            if i == n-1 and j == m-1:
                return max(1,1-dungeon[i][j])
            return max(min(dfs(i+1,j), dfs(i,j+1)) - dungeon[i][j],1)
        # ans = dfs(len(dungeon)-1,len(dungeon[0])-1)
        return dfs(0,0)


# @lc code=end

if __name__ == "__main__":
    dungeon: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().calculateMinimumHP(dungeon)
    print("\noutput:", serialize(ans, "integer"))
