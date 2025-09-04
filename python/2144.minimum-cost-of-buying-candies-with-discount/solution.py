# Created by woxQAQ at 2025/09/03 21:13
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimum-cost-of-buying-candies-with-discount/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        for i in range(2, len(cost), 3):
            cost[i] = 0
        return sum(cost)


# @lc code=end

if __name__ == "__main__":
    cost: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumCost(cost)
    print("\noutput:", serialize(ans, "integer"))
