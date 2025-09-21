# Created by woxQAQ at 2025/09/20 21:53
# leetgo: 1.4.15
# https://leetcode.cn/problems/UEcfPD/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def perfectMenu(
        self,
        materials: List[int],
        cookbooks: List[List[int]],
        attribute: List[List[int]],
        limit: int,
    ) -> int:
        res = -1

        def dfs(i, full, deli):
            if i == len(cookbooks):
                nonlocal res
                if full >= limit:
                    res = max(res, deli)
                return
            dfs(i + 1, full, deli)
            if all(
                materials[j] >= cookbooks[i][j] for j in range(len(materials))
            ):
                for j in range(len(materials)):
                    materials[j] -= cookbooks[i][j]
                dfs(i + 1, full + attribute[i][1], deli + attribute[i][0])
                for j in range(len(materials)):
                    materials[j] += cookbooks[i][j]

        dfs(0, 0, 0)
        return res


# @lc code=end

if __name__ == "__main__":
    materials: List[int] = deserialize("List[int]", read_line())
    cookbooks: List[List[int]] = deserialize("List[List[int]]", read_line())
    attribute: List[List[int]] = deserialize("List[List[int]]", read_line())
    limit: int = deserialize("int", read_line())
    ans = Solution().perfectMenu(materials, cookbooks, attribute, limit)
    print("\noutput:", serialize(ans, "integer"))
