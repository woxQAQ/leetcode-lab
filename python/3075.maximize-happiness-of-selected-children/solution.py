# Created by woxQAQ at 2025/09/02 14:38
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximize-happiness-of-selected-children/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        for i, x in enumerate(happiness[:k]):
            if x - i <= 0:
                break
            res += x - i
        return res


# @lc code=end

if __name__ == "__main__":
    happiness: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumHappinessSum(happiness, k)
    print("\noutput:", serialize(ans, "long"))
