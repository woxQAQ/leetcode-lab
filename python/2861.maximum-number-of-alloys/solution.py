# Created by woxQAQ at 2025/08/31 20:43
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximum-number-of-alloys/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxNumberOfAlloys(
        self,
        n: int,
        k: int,
        budget: int,
        composition: List[List[int]],
        stock: List[int],
        cost: List[int],
    ) -> int:
        # k=2, [1,1,1], [1,1,10]
        # 6, 33
        res = 0
        for comp in composition:
            l, r = 0, min(stock) + budget + 1

            def check(m):
                money = 0
                for s, base, c in zip(stock, comp, cost):
                    if s < base * m:
                        money += (base * m - s) * c
                        if money > budget:
                            return False

                return True

            while l < r - 1:
                m = (l + r) // 2
                if check(m):
                    l = m
                else:
                    r = m
            res = max(res, l)
        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    budget: int = deserialize("int", read_line())
    composition: List[List[int]] = deserialize("List[List[int]]", read_line())
    stock: List[int] = deserialize("List[int]", read_line())
    cost: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxNumberOfAlloys(n, k, budget, composition, stock, cost)
    print("\noutput:", serialize(ans, "integer"))
