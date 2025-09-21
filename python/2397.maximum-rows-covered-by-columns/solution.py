# Created by woxQAQ at 2025/09/20 22:11
# leetgo: 1.4.15
# https://leetcode.cn/problems/maximum-rows-covered-by-columns/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        selected = []
        max_covered = 0
        all_zero_rows = set(
            [i for i, row in enumerate(matrix) if all(num == 0 for num in row)]
        )

        def check(i):
            if i in all_zero_rows:
                return True
            row = matrix[i]
            for col in list(range(len(matrix[0]))):
                if row[col] == 1 and col not in selected:
                    return False
            return True

        def dfs(i):
            if len(selected) == numSelect:
                tmp = 0
                for row in range(len(matrix)):
                    if check(row):
                        tmp += 1
                nonlocal max_covered
                max_covered = max(max_covered, tmp)
                return

            if i == len(matrix[0]):
                return

            selected.append(i)
            dfs(i + 1)
            selected.pop()
            dfs(i + 1)

        dfs(0)
        return max_covered


# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    numSelect: int = deserialize("int", read_line())
    ans = Solution().maximumRows(matrix, numSelect)
    print("\noutput:", serialize(ans, "integer"))
