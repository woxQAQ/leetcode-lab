# Created by woxQAQ at 2025/09/03 12:05
# leetgo: 1.4.13
# https://leetcode.cn/problems/uOAnQW/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort(reverse=True)
        s = sum(cards[:cnt])
        if s % 2 == 0:
            return s

        def replace(x):
            for v in cards[cnt:]:
                if v % 2 != x % 2:
                    return s - x + v
            return 0

        x = cards[cnt - 1]
        ans = replace(x)
        for v in cards[cnt - 1 :: -1]:
            if v % 2 != x % 2:
                ans = max(ans, replace(v))
                break
        return ans


# @lc code=end

if __name__ == "__main__":
    cards: List[int] = deserialize("List[int]", read_line())
    cnt: int = deserialize("int", read_line())
    ans = Solution().maximumScore(cards, cnt)
    print("\noutput:", serialize(ans, "integer"))
