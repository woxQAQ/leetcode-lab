# Created by woxQAQ at 2025/09/04 16:17
# leetgo: 1.4.15
# https://leetcode.cn/problems/insert-interval/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        # find the first interval1 that
        # interval1[1] >= newInterval[0]
        #
        # find the last interval2 that
        # interval2[0] <= newInterval[1]
        #
        # then interval between i1 and i2 should be merged into
        # [interval1[0], max(interval2[1], newInterval[1])]
        l, r = newInterval
        lans, rans = [], []
        for i in intervals:
            if i[1] < newInterval[0]:
                lans.append(i)
            elif i[0] > newInterval[1]:
                rans.append(i)
            else:
                l = min(l, i[0])
                r = max(r, i[1])

        return lans + [[l, r]] + rans


# @lc code=end

if __name__ == "__main__":
    intervals: List[List[int]] = deserialize("List[List[int]]", read_line())
    newInterval: List[int] = deserialize("List[int]", read_line())
    ans = Solution().insert(intervals, newInterval)
    print("\noutput:", serialize(ans, "integer[][]"))
