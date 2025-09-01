# Created by woxQAQ at 2025/09/01 13:19
# leetgo: 1.4.13
# https://leetcode.cn/problems/sell-diminishing-valued-colored-balls/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        l, r = 0, max(inventory)
        mod = 10**9 + 7
        while l < r - 1:
            m = (l + r) // 2
            if sum(x - m for x in inventory if x > m) > orders:
                l = m
            else:
                r = m
        res = sum((r + 1 + x) * (x - r) // 2 for x in inventory if x > r)
        orders -= sum(x - r for x in inventory if x > r)
        res += orders * r
        return res % mod


# @lc code=end

if __name__ == "__main__":
    inventory: List[int] = deserialize("List[int]", read_line())
    orders: int = deserialize("int", read_line())
    ans = Solution().maxProfit(inventory, orders)
    print("\noutput:", serialize(ans, "integer"))
