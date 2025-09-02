# Created by woxQAQ at 2025/09/02 14:17
# leetgo: 1.4.13
# https://leetcode.cn/problems/reduce-array-size-to-the-half/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = sorted(Counter(arr).values(), reverse=True)
        res = 0
        total = len(arr)
        temp = total
        for c in cnt:
            res += 1
            temp -= c
            if temp <= total // 2:
                break
        return res


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minSetSize(arr)
    print("\noutput:", serialize(ans, "integer"))
