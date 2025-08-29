# Created by woxQAQ at 2025/08/29 18:31
# leetgo: 1.4.15
# https://leetcode.cn/problems/count-the-number-of-good-subarrays/

from collections import defaultdict
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ans = l = 0
        cnt = defaultdict(int)
        pairs = 0
        for x in nums:
            pairs += cnt[x]
            cnt[x] += 1
            while pairs >= k:
                cnt[nums[l]] -= 1
                pairs -= cnt[nums[l]]
                l += 1
            ans += l

        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().countGood(nums, k)
    print("\noutput:", serialize(ans, "long"))
