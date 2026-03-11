# Created by woxQAQ at 2026/03/11 23:08
# leetgo: 1.4.16
# https://leetcode.cn/problems/container-with-most-water/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        ans=0
        while l < r:
            area = (r-l)*min(height[l],height[r])
            ans=max(area,ans)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ans
# @lc code=end

if __name__ == "__main__":
    height: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxArea(height)
    print("\noutput:", serialize(ans, "integer"))
