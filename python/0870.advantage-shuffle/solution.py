# Created by woxQAQ at 2025/09/04 10:52
# leetgo: 1.4.13
# https://leetcode.cn/problems/advantage-shuffle/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        n = len(nums2)
        indice2 = sorted(range(n), key=lambda i: nums2[i])
        ans = [0] * n
        l, r = 0, n - 1
        for num in nums1:
            if num > nums2[indice2[l]]:
                ans[indice2[l]] = num
                l += 1
            else:
                ans[indice2[r]] = num
                r -= 1

        return ans


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().advantageCount(nums1, nums2)
    print("\noutput:", serialize(ans, "integer[]"))
