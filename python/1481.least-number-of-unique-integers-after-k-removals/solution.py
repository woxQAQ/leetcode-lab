# Created by woxQAQ at 2025/09/02 13:36
# leetgo: 1.4.13
# https://leetcode.cn/problems/least-number-of-unique-integers-after-k-removals/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = sorted(Counter(arr).values())
        res = len(cnt)
        for i, x in enumerate(cnt):
            if k >= x:
                k -= x
                res -= 1
        return res


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findLeastNumOfUniqueInts(arr, k)
    print("\noutput:", serialize(ans, "integer"))
