# Created by woxQAQ at 2026/03/12 02:35
# leetgo: 1.4.16
# https://leetcode.cn/problems/sliding-window-maximum/
from collections import deque

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 单调队列模板
        # 单调队列适应于窗口范围内的最值问题
        # 相对的，单调栈维护的是当前数据的历史值
        #
        # 关注两个值
        # q[0] 
        # q[-1]
        q=deque()
        ans = [0] * (len(nums)-k+1)
        # 最大值，需要递减队列
        for i,x in enumerate(nums):
            # <= 递减队列
            while len(q) > 0 and nums[q[-1]] <= x:
                q.pop()
            q.append(i)

            # 检查左窗口
            left = i-k+1

            # 最大值是否退出窗口
            if q[0] < left:
                q.popleft()
            # 以 left 为左边界的窗口最大值为当前单调队列维护的最值
            if left >= 0:
                ans[left]= nums[q[0]]
        return ans

        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxSlidingWindow(nums, k)
    print("\noutput:", serialize(ans, "integer[]"))
