# Created by woxQAQ at 2025/09/04 12:49
# leetgo: 1.4.13
# https://leetcode.cn/problems/most-profit-assigning-work/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        jobs = sorted(zip(difficulty, profit))
        max_profit = 0
        ans = 0
        i = 0
        for w in sorted(worker):
            # 经过排序后，当前worker一定可以完成上一个worker完成的最大收益任务
            # i 指向当前难度最大的任务
            # 问题是任务 i 是否可以被当前worker完成
            while i < len(jobs) and jobs[i][0] <= w:
                max_profit = max(max_profit, jobs[i][1])
                i += 1
            ans += max_profit
        return ans


# @lc code=end

if __name__ == "__main__":
    difficulty: List[int] = deserialize("List[int]", read_line())
    profit: List[int] = deserialize("List[int]", read_line())
    worker: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfitAssignment(difficulty, profit, worker)
    print("\noutput:", serialize(ans, "integer"))
