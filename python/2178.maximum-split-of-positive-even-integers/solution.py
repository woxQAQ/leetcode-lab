# Created by woxQAQ at 2025/09/03 08:37
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximum-split-of-positive-even-integers/

from collections import defaultdict
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        total = 0
        cur = 0
        if finalSum % 2 != 0:
            return []
        res = []
        s = defaultdict(int)
        while total < finalSum:
            cur += 2
            total += cur
            if total > finalSum:
                cur += finalSum - total
            res.append(cur)
            s[cur] += 1
        if s[res[-1]] > 1:
            res[-2] += res[-1]
            res.pop()
        return res


# @lc code=end

if __name__ == "__main__":
    finalSum: int = deserialize("int", read_line())
    ans = Solution().maximumEvenSplit(finalSum)
    print("\noutput:", serialize(ans, "long[]"))
