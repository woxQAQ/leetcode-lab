# Created by woxQAQ at 2025/08/25 01:01
# leetgo: 1.4.15
# https://leetcode.cn/problems/number-of-paths-with-max-score/

"""
1301. 最大得分的路径数目 (Hard)
给你一个正方形字符数组 `board` ，你从数组最右下方的字符 `'S'` 出发。

你的目标是到达数组最左上角的字符 `'E'` ，数组剩余的部分为数字字符 `1, 2, ..., 9` 或者障碍 `'X'`。在
每一步移动中，你可以向上、向左或者左上方移动，可以移动的前提是到达的格子没有障碍。

一条路径的 「得分」 定义为：路径上所有数字的和。

请你返回一个列表，包含两个整数：第一个整数是 「得分」 的最大值，第二个整数是得到最大得分的方案数，请
把结果对 **`10^9 + 7`** **取余**。

如果没有任何路径可以到达终点，请返回 `[0, 0]` 。

**示例 1：**

```
输入：board = ["E23","2X2","12S"]
输出：[7,1]
```

**示例 2：**

```
输入：board = ["E12","1X1","21S"]
输出：[4,2]
```

**示例 3：**

```
输入：board = ["E11","XXX","11S"]
输出：[0,0]
```

**提示：**

- `2 <= board.length == board[i].length <= 100`

"""

from functools import cache
from typing import *
from math import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        X = 'X'
        MOD = 10**9 + 7

        """
            [
            E,1,2,
            3,X,4,
            5,6,S,
            ]
        """

        @cache
        def dfs(i,j):
            if i ==0 and j == 0:
                return [0,1]
            if i < 0 or j < 0:
                return [-inf,0]
            if board[i][j]=='X':
                return [-inf,0]
            res = [-inf,0]
            for x,y in [(i-1,j),(i,j-1),(i-1,j-1)]:
                score,ways = dfs(x,y)
                if score > res[0]:
                    res = [score,ways]
                elif score == res[0]:
                    res[1] = (ways+res[1])%MOD
            res[0] += int(board[i][j]) if board[i][j] != 'S' else 0
            return res
        n,m = len(board),len(board[0])
        # res = dfs(n-1,m-1)
        # if res[0] == -inf:
        #     return [0,0]
        # return [res[0],res[1]%MOD]
        dp = [[[0, 0] for _ in range(m)] for _ in range(n)]
        dp[0][0] = [0,1]
        for i, line in enumerate(board):
            for j, char in enumerate(line):
                if char == 'X':
                    dp[i][j] = [-inf,0]
                    continue
                elif char == 'E':
                    continue
                res = [-inf,0]
                for x,y in [(i-1,j),(i,j-1),(i-1,j-1)]:
                    if x < 0 or y < 0:
                        continue
                    score,ways = dp[x][y]
                    if score > res[0]:
                        res = [score,ways]
                    elif score == res[0]:
                        res[1] = (ways+res[1])%MOD
                dp[i][j] = [res[0]+(int(board[i][j]) if board[i][j] != 'S' else 0),res[1]]
        return dp[n-1][m-1] if dp[n-1][m-1][0] != -inf else [0,0]


# @lc code=end

if __name__ == "__main__":
    board: List[str] = deserialize("List[str]", read_line())
    ans = Solution().pathsWithMaxScore(board)
    print("\noutput:", serialize(ans, "integer[]"))
