# Created by woxQAQ at 2025/09/02 16:39
# leetgo: 1.4.13
# https://leetcode.cn/problems/find-subsequence-of-length-k-with-the-largest-sum/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        return [
            nums[i]
            for i in sorted(
                sorted(range(len(nums)), key=lambda i: nums[i], reverse=True)[:k]
            )
        ]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxSubsequence(nums, k)
    print("\noutput:", serialize(ans, "integer[]"))
