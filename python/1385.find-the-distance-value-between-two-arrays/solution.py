# Created by woxQAQ at 2025/08/29 23:08
# leetgo: 1.4.13
# https://leetcode.cn/problems/find-the-distance-value-between-two-arrays/

from bisect import bisect_left
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # -d <= arr1[i] - arr2[j] <= d
        # arr2[j] -d <= arr1[i] <= arr2[j] + d
        arr2.sort()
        ans = 0
        for tar in arr1:
            i1 = bisect_left(arr2, tar - d)
            if i1 == len(arr2) or arr2[i1] > tar + d:
                ans += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    arr1: List[int] = deserialize("List[int]", read_line())
    arr2: List[int] = deserialize("List[int]", read_line())
    d: int = deserialize("int", read_line())
    ans = Solution().findTheDistanceValue(arr1, arr2, d)
    print("\noutput:", serialize(ans, "integer"))
