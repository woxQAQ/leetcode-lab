# Created by woxQAQ at 2025/08/31 04:49
# leetgo: 1.4.13
# https://leetcode.cn/problems/find-k-closest-elements/

from bisect import bisect_left
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        a, b = abs(arr[l] - x), abs(arr[r] - x)
        while r - l + 1 != k:
            if a <= b:
                r -= 1
                b = abs(arr[r] - x)
            else:
                l += 1
                a = abs(arr[l] - x)
        return arr[l : r + 1]


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    x: int = deserialize("int", read_line())
    ans = Solution().findClosestElements(arr, k, x)
    print("\noutput:", serialize(ans, "integer[]"))
