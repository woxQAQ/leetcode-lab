# Created by woxQAQ at 2025/08/31 14:40
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximum-candies-allocated-to-k-children/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        r = min(sum(candies) // k, max(candies)) + 1
        l = 0
        while l < r - 1:
            mid = (l + r) // 2
            if sum(candy // mid for candy in candies) >= k:
                l = mid
            else:
                r = mid
        return l


# @lc code=end

if __name__ == "__main__":
    candies: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumCandies(candies, k)
    print("\noutput:", serialize(ans, "integer"))
