# Created by woxQAQ at 2025/08/31 16:08
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimum-time-to-complete-trips/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        mint = min(time)
        l, r = mint - 1, mint * totalTrips
        while l < r - 1:
            mid = (l + r) // 2
            if sum(mid // t for t in time) >= totalTrips:
                r = mid
            else:
                l = mid
        return r


# @lc code=end

if __name__ == "__main__":
    time: List[int] = deserialize("List[int]", read_line())
    totalTrips: int = deserialize("int", read_line())
    ans = Solution().minimumTime(time, totalTrips)
    print("\noutput:", serialize(ans, "long"))
