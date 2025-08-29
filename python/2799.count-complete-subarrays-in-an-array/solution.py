# Created by woxQAQ at 2025/08/29 18:29
# leetgo: 1.4.15
# https://leetcode.cn/problems/count-complete-subarrays-in-an-array/

from collections import defaultdict
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        cnt = len(set(nums))
        cnt_s = defaultdict(int)
        ans = l = 0
        for r, x in enumerate(nums):
            cnt_s[x] += 1
            while len(cnt_s) == cnt:
                cnt_s[nums[l]] -= 1
                if cnt_s[nums[l]] == 0:
                    del cnt_s[nums[l]]
                l += 1
            ans += l
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countCompleteSubarrays(nums)
    print("\noutput:", serialize(ans, "integer"))
