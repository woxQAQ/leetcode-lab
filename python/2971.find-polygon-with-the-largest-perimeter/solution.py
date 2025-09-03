# Created by woxQAQ at 2025/09/03 08:27
# leetgo: 1.4.13
# https://leetcode.cn/problems/find-polygon-with-the-largest-perimeter/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        # 50,12,5,3,2,1,1
        s = 0
        ans = -1
        for x in nums:
            s += x
            if s > 2 * x:
                ans = s
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().largestPerimeter(nums)
    print("\noutput:", serialize(ans, "long"))
