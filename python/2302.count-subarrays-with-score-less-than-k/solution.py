# Created by woxQAQ at 2025/08/29 17:25
# leetgo: 1.4.15
# https://leetcode.cn/problems/count-subarrays-with-score-less-than-k/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = l = 0
        s = 0
        for r, num in enumerate(nums):
            s += num
            while s * (r - l + 1) >= k:
                s -= nums[l]
                l += 1
            ans += r - l + 1
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().countSubarrays(nums, k)
    print("\noutput:", serialize(ans, "long"))
