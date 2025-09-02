# Created by woxQAQ at 2025/09/02 07:03
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimize-the-maximum-difference-of-pairs/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        l, r = -1, nums[-1] - nums[0]

        def check(mid):
            # [1,1,2,3,7,10]
            #
            i = 0
            cnt = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= mid:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= p

        while l < r - 1:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m
        return r


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    p: int = deserialize("int", read_line())
    ans = Solution().minimizeMax(nums, p)
    print("\noutput:", serialize(ans, "integer"))
