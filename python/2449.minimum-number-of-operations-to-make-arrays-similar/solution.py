# Created by woxQAQ at 2025/09/04 13:06
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimum-number-of-operations-to-make-arrays-similar/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        """
        [2,10,14]
        [6,8,12]

        [-5,-1,2]
        [-3,-1,4]
        """
        nums = [num if num % 2 == 0 else -num for num in nums]
        target = [t if t % 2 == 0 else -t for t in target]
        nums.sort()
        target.sort()

        return sum(abs(nums[i] - target[i]) for i in range(len(nums))) // 4


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: List[int] = deserialize("List[int]", read_line())
    ans = Solution().makeSimilar(nums, target)
    print("\noutput:", serialize(ans, "long"))
