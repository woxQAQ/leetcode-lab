# Created by woxQAQ at 2025/09/03 11:05
# leetgo: 1.4.13
# https://leetcode.cn/problems/eat-pizzas/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        # 由于奇数天每次都取最大值
        # 因此我们先拿所有奇数天的
        # pizzas[r-1] == pizzas[r], 拿前三个和最后一个
        #
        # 偶数天，拿前两个和后两个
        pizzas.sort()
        n = len(pizzas)
        l, r = 0, n - 1
        res = 0
        # 1,2,2,2,2,3,3,3,4,4,5,5
        for _ in range(1, n // 4 + 1, 2):
            res += pizzas[r]
            l += 3
            r -= 1
        for _ in range(2, n // 4 + 1, 2):
            res += pizzas[r - 1]
            l += 2
            r -= 2
        return res


# @lc code=end

if __name__ == "__main__":
    pizzas: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxWeight(pizzas)
    print("\noutput:", serialize(ans, "long"))
