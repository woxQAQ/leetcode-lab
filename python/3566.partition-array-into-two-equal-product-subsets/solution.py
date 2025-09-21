# Created by woxQAQ at 2025/09/20 21:12
# leetgo: 1.4.15
# https://leetcode.cn/problems/partition-array-into-two-equal-product-subsets/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        def dfs(i, product1, product2):
            if i == len(nums):
                return product1 == product2 == target
            return dfs(i + 1, product1 * nums[i], product2) or dfs(
                i + 1, product1, product2 * nums[i]
            )

        return dfs(0, 1, 1)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().checkEqualPartitions(nums, target)
    print("\noutput:", serialize(ans, "boolean"))
