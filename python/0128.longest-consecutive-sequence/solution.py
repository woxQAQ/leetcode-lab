# Created by woxQAQ at 2026/03/11 21:16
# leetgo: 1.4.16
# https://leetcode.cn/problems/longest-consecutive-sequence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m=set()
        for num in nums:
            m.add(num)
        res = 0
        for x in m:
            if x-1 in m:
                continue
            y=x+1
            while y in m:
                y+=1
            res = max(res, y-x)
        return res
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestConsecutive(nums)
    print("\noutput:", serialize(ans, "integer"))
