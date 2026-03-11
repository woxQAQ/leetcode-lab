# Created by woxQAQ at 2026/03/12 00:27
# leetgo: 1.4.16
# https://leetcode.cn/problems/3sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            j = i+1
            k= n-1
            while j < k:
                if j > i + 1 and nums[j] == nums[j-1]:
                    j+=1
                    continue
                while j < k and nums[j]+nums[k] > target:
                    k-=1
                    continue
                if j != k and nums[j]+nums[k] ==target:
                    ans.append([nums[i],nums[j],nums[k]])       
                j+=1
        return ans

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().threeSum(nums)
    print("\noutput:", serialize(ans, "integer[][]"))
