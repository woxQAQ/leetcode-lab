# Created by woxQAQ at 2026/03/11 22:50
# leetgo: 1.4.16
# https://leetcode.cn/problems/move-zeroes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index_0= 0
        for i,v in enumerate(nums):
            if v != 0:
                nums[index_0],nums[i] = nums[i] ,nums[index_0]       
                index_0+=1

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    moveZeroes(nums)
    ans = nums
    print("\noutput:", serialize(ans, "List[int]"))
