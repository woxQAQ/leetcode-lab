# Created by woxQAQ at 2025/08/29 22:14
# leetgo: 1.4.13
# https://leetcode.cn/problems/successful-pairs-of-spells-and-potions/

from bisect import bisect_left
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        return [
            len(potions) - bisect_left(potions, success / spell) for spell in spells
        ]


# @lc code=end

if __name__ == "__main__":
    spells: List[int] = deserialize("List[int]", read_line())
    potions: List[int] = deserialize("List[int]", read_line())
    success: int = deserialize("int", read_line())
    ans = Solution().successfulPairs(spells, potions, success)
    print("\noutput:", serialize(ans, "integer[]"))
