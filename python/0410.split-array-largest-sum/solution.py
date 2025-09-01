# Created by woxQAQ at 2025/09/01 13:48
# leetgo: 1.4.13
# https://leetcode.cn/problems/split-array-largest-sum/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # [1,2,3,4,5,6] k = 2
        # C51=  5
        # [1,2,3,4] k = 3
        # 1,2,34; 12,3,4; 1,23,4
        # C32
        #
        # C(len(nums))(k-1)
        def check(mid):
            cnt = 1
            cur = 0
            for num in nums:
                if cur + num <= mid:
                    cur += num
                    continue
                if cnt == k:
                    return False
                cnt += 1
                cur = num
            return True

        l, r = max(nums) - 1, sum(nums)
        while l < r - 1:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid

        return r


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().splitArray(nums, k)
    print("\noutput:", serialize(ans, "integer"))
