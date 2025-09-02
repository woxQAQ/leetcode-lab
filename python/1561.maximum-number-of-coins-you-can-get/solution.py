# Created by woxQAQ at 2025/09/02 15:56
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximum-number-of-coins-you-can-get/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)

        ans = 0
        # [8,7,4,2,2,1]
        # 1. [8,7,2]
        #
        # [9,8,7,6,5,4,3,2,1] X
        # [9,8,1,7,6,2,5,4,3]
        # 8+6+4=18
        #
        # 拿掉第一个和最后一个，剩下的最大值就是我的
        l, r = 1, len(piles) - 1
        while l < r:
            ans += piles[l]
            l += 2
            r -= 1
        return ans


# @lc code=end

if __name__ == "__main__":
    piles: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxCoins(piles)
    print("\noutput:", serialize(ans, "integer"))
