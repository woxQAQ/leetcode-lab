# Created by woxQAQ at 2026/03/11 22:52
# leetgo: 1.4.16
# https://leetcode.cn/problems/trapping-rain-water/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = pre = suf = 0
        l,r=0,len(height)-1
        while l < r:
            pre = max(pre,height[l])
            suf = max(suf,height[r])
            if pre < suf:
                ans += pre - height[l]
                l+=1
            else:
                ans += suf-height[r]
                r-=1
        return ans
        

# @lc code=end

if __name__ == "__main__":
    height: List[int] = deserialize("List[int]", read_line())
    ans = Solution().trap(height)
    print("\noutput:", serialize(ans, "integer"))
