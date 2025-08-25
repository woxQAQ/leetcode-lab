# Created by woxQAQ at 2025/08/25 00:27
# leetgo: 1.4.15
# https://leetcode.cn/problems/maximum-non-negative-product-in-a-matrix/

from functools import cache
from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        """
        最大非负积
        """
        # @cache
        # def dfs(i,j,flag):
        #     if i == 0 and j == 0 :
        #         return grid[i][j]
        #     if i < 0 or j < 0:
        #         return 1 if flag else -1
        #     if grid[i][j]< 0:
        #         # flag = 1 flag * grid[i][j] > 0, max
        #         _func = max if flag else min
        #         return _func(dfs(i-1,j,not flag),dfs(i,j-1,not flag)) * grid[i][j]
        #     else:
        #         _func = min if flag else max
        #         return _func(dfs(i-1,j,flag),dfs(i,j-1,flag)) * grid[i][j]
        n,m = len(grid),len(grid[0])
        MOD = 10**9 + 7
        # return -1 if dfs(n-1,m-1,False) < 0 else dfs(n-1,m-1,False) % MOD

        dpmax = [[0]*m for _ in range(n)]
        dpmin = [[0]*m for _ in range(n)]
        dpmax[0][0] = dpmin[0][0] = grid[0][0]
        for i in range(1,n):
            dpmax[i][0] = dpmax[i-1][0] * grid[i][0]
            dpmin[i][0] = dpmin[i-1][0] * grid[i][0]
        for j in range(1,m):
            dpmax[0][j] = dpmax[0][j-1] * grid[0][j]
            dpmin[0][j] = dpmin[0][j-1] * grid[0][j]
        for i in range(1,n):
            for j in range(1,m):
                if grid[i][j] < 0:
                    dpmax[i][j] = min(dpmin[i-1][j],dpmin[i][j-1]) * grid[i][j]
                    dpmin[i][j] = max(dpmax[i-1][j],dpmax[i][j-1]) * grid[i][j]
                else:
                    dpmax[i][j] = max(dpmax[i-1][j],dpmax[i][j-1]) * grid[i][j]
                    dpmin[i][j] = min(dpmin[i-1][j],dpmin[i][j-1]) * grid[i][j]
        return -1 if dpmax[n-1][m-1] < 0 else dpmax[n-1][m-1] % MOD

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxProductPath(grid)
    print("\noutput:", serialize(ans, "integer"))
