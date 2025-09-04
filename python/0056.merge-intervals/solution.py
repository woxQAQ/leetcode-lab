# Created by woxQAQ at 2025/09/04 14:34
# leetgo: 1.4.13
# https://leetcode.cn/problems/merge-intervals/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        for i in intervals:
            if ans and i[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], i[1])
            else:
                ans.append(i)
        return ans


# @lc code=end

if __name__ == "__main__":
    intervals: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().merge(intervals)
    print("\noutput:", serialize(ans, "integer[][]"))
