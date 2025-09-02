# Created by woxQAQ at 2025/09/02 13:50
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimum-subsequence-in-non-increasing-order/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        ans = []
        total = sum(nums)
        tmp = 0
        for num in nums:
            ans.append(num)
            tmp += num
            if tmp > total - tmp:
                break
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minSubsequence(nums)
    print("\noutput:", serialize(ans, "integer[]"))
