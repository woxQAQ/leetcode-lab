# Created by woxQAQ at 2025/09/01 18:29
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimize-maximum-component-cost/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        if k >= n:
            return 0
        l, r = 0, max(edge[2] for edge in edges)

        def check(mid):
            uf = list(range(n))
            count = n

            def find(x):
                if uf[x] != x:
                    uf[x] = find(uf[x])
                return uf[x]

            for u, v, w in edges:
                if w <= mid:
                    ru, rv = find(u), find(v)
                    if ru != rv:
                        uf[ru] = rv
                        count -= 1
            return count

        while l < r - 1:
            mid = (l + r) // 2
            if check(mid) <= k:
                r = mid
            else:
                l = mid
        return r


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minCost(n, edges, k)
    print("\noutput:", serialize(ans, "integer"))
