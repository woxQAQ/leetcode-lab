# Created by woxQAQ at 2026/03/25 02:22
# leetgo: 1.4.16
# https://leetcode.cn/problems/set-matrix-zeroes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_zeros = 0 in matrix[0]
        first_column_zeros = any(row[0]==0 for row in matrix)
        m,n = len(matrix),len(matrix[0])
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] ==0:
                    matrix[i][j] = 0
        if first_column_zeros:
            for row in matrix:
                row[0] = 0
        if first_row_zeros:
            for i in range(n):
                matrix[0][i]=0
        

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    setZeroes(matrix)
    ans = matrix
    print("\noutput:", serialize(ans, "List[List[int]]"))
