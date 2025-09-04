# Created by woxQAQ at 2025/09/04 14:13
# leetgo: 1.4.13
# https://leetcode.cn/problems/can-place-flowers/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
                if n <= 0:
                    return True
        return n <= 0


# @lc code=end

if __name__ == "__main__":
    flowerbed: List[int] = deserialize("List[int]", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().canPlaceFlowers(flowerbed, n)
    print("\noutput:", serialize(ans, "boolean"))
