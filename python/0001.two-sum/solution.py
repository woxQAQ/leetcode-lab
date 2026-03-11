# Created by woxQAQ at 2026/03/11 17:23
# leetgo: 1.4.16
# https://leetcode.cn/problems/two-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def twoSum(self, nums: List[int], target: int) -> list[int]:
        m = {}
        for i,n in enumerate(nums):
            if target - n in m:
                return [i,m[target-n]]
            m[n] = i
        return []
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().twoSum(nums, target)
    print("\noutput:", serialize(ans, "integer[]"))
