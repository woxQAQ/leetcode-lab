# Created by woxQAQ at 2025/08/29 20:00
# leetgo: 1.4.15
# https://leetcode.cn/problems/subarrays-with-k-different-integers/

from collections import defaultdict
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def f(k):
            ans = l = 0
            cnt_k = defaultdict(int)
            for r, num in enumerate(nums):
                cnt_k[num] += 1
                while len(cnt_k) == k:
                    cnt_k[nums[l]] -= 1
                    if cnt_k[nums[l]] == 0:
                        del cnt_k[nums[l]]
                    l += 1
                ans += l
            return ans

        return f(k) - f(k + 1)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().subarraysWithKDistinct(nums, k)
    print("\noutput:", serialize(ans, "integer"))
