# Created by woxQAQ at 2025/09/02 14:24
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximum-units-on-a-truck/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        for [num, box] in boxTypes:
            if truckSize >= num:
                ans += num * box
                truckSize -= num
            else:
                ans += truckSize * box
                break
        return ans


# @lc code=end

if __name__ == "__main__":
    boxTypes: List[List[int]] = deserialize("List[List[int]]", read_line())
    truckSize: int = deserialize("int", read_line())
    ans = Solution().maximumUnits(boxTypes, truckSize)
    print("\noutput:", serialize(ans, "integer"))
