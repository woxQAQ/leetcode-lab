# Created by woxQAQ at 2025/08/29 19:26
# leetgo: 1.4.15
# https://leetcode.cn/problems/count-number-of-nice-subarrays/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def f(k):
            ans = l = cnt = 0
            for r, x in enumerate(nums):
                cnt += x % 2 == 1
                while l <= r and cnt == k:
                    cnt -= nums[l] % 2 == 1
                    l += 1
                ans += l
            return ans

        return f(k) - f(k + 1)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numberOfSubarrays(nums, k)
    print("\noutput:", serialize(ans, "integer"))
