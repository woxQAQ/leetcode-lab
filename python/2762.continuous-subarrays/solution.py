# Created by woxQAQ at 2025/08/29 17:39
# leetgo: 1.4.15
# https://leetcode.cn/problems/continuous-subarrays/

from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        cnt = Counter()
        ans = l = 0
        for r, num in enumerate(nums):
            cnt[num] += 1
            while max(cnt) - min(cnt) > 2:
                cnt[nums[l]] -= 1
                if cnt[nums[l]] == 0:
                    del cnt[nums[l]]
                l += 1
            ans += r - l + 1

        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().continuousSubarrays(nums)
    print("\noutput:", serialize(ans, "long"))
