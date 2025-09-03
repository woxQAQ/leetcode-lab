# Created by woxQAQ at 2025/09/03 07:45
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximum-element-after-decreasing-and-rearranging/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff > 1:
                arr[i] = arr[i - 1] + 1
        return arr[-1]


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumElementAfterDecrementingAndRearranging(arr)
    print("\noutput:", serialize(ans, "integer"))
