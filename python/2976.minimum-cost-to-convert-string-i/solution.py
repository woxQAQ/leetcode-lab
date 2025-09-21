# Created by woxQAQ at 2025/09/08 19:58
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-cost-to-convert-string-i/

from math import cos, inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        dp = [[inf] * 26 for _ in range(26)]
        for i in range(26):
            dp[i][i] = 0
        for x, y, wt in zip(original, changed, cost):
            x = ord(x) - ord("a")
            y = ord(y) - ord("a")
            dp[x][y] = min(dp[x][y], wt)

        for k in range(26):
            for i in range(26):
                if dp[i][k] == inf:
                    continue
                for j in range(26):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

        ans = sum(
            dp[ord(x) - ord("a")][ord(y) - ord("a")]
            for x, y in zip(source, target)
        )

        return ans if ans != inf else -1


# @lc code=end

if __name__ == "__main__":
    source: str = deserialize("str", read_line())
    target: str = deserialize("str", read_line())
    original: List[str] = deserialize("List[str]", read_line())
    changed: List[str] = deserialize("List[str]", read_line())
    cost: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumCost(source, target, original, changed, cost)
    print("\noutput:", serialize(ans, "long"))
