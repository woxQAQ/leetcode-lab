# Created by woxQAQ at 2025/09/03 18:24
# leetgo: 1.4.13
# https://leetcode.cn/problems/reschedule-meetings-for-maximum-free-time-ii/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: List[int], endTime: List[int]
    ) -> int:
        n = len(startTime)
        pre = [0] * n
        suf = [0] * n
        pre[0] = startTime[0]
        suf[n - 1] = eventTime - endTime[-1]
        for i in range(1, n):
            pre[i] = max(pre[i - 1], startTime[i] - endTime[i - 1])
        for i in range(n - 2, -1, -1):
            suf[i] = max(suf[i + 1], startTime[i + 1] - endTime[i])

        ans = 0
        for i in range(n):
            l = 0 if i == 0 else endTime[i - 1]
            r = eventTime if i == n - 1 else startTime[i + 1]
            w = endTime[i] - startTime[i]
            ans = max(ans, r - l - w)
            if i and pre[i - 1] >= w:
                ans = max(r - l, ans)
            elif i < n - 1 and suf[i + 1] >= w:
                ans = max(ans, r - l)
        return ans


# @lc code=end

if __name__ == "__main__":
    eventTime: int = deserialize("int", read_line())
    startTime: List[int] = deserialize("List[int]", read_line())
    endTime: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxFreeTime(eventTime, startTime, endTime)
    print("\noutput:", serialize(ans, "integer"))
