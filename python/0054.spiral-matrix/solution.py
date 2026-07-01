# Created by woxQAQ at 2026/03/25 03:11
# leetgo: 1.4.16
# https://leetcode.cn/problems/spiral-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin

D = (0,1),(1,0),(0,-1),(-1,0)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        cursor=(0,0)
        di=0
        res = []
        m,n=len(matrix),len(matrix[0])
        x,y=0,0
        for _ in range(m*n):
            res.append(matrix[x][y])
            matrix[x][y]=None
            dx,dy=D[di]
            tx=x+dx
            ty=y+dy
            if tx < 0 or tx >= m or ty < 0 or ty >= n or matrix[tx][ty] is None:
                di = (di + 1) % 4

            dx,dy=D[di]
            x+=dx
            y+=dy
        return res
# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().spiralOrder(matrix)
    print("\noutput:", serialize(ans, "integer[]"))
