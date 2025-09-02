# Created by woxQAQ at 2025/09/02 13:13
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximum-ice-cream-bars/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for c in costs:
            if coins > 0 and coins - c >= 0:
                coins -= c
                ans += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    costs: List[int] = deserialize("List[int]", read_line())
    coins: int = deserialize("int", read_line())
    ans = Solution().maxIceCream(costs, coins)
    print("\noutput:", serialize(ans, "integer"))
