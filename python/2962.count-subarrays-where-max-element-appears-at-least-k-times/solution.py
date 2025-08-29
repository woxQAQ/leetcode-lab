# Created by woxQAQ at 2025/08/29 18:17
# leetgo: 1.4.15
# https://leetcode.cn/problems/count-subarrays-where-max-element-appears-at-least-k-times/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        l = ans = 0
        cnt_max = 0
        for r, x in enumerate(nums):
            if x == max_val:
                cnt_max += 1
            while cnt_max == k:
                if nums[l] == max_val:
                    cnt_max -= 1
                l += 1
            ans += l
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().countSubarrays(nums, k)
    print("\noutput:", serialize(ans, "long"))
