# Created by woxQAQ at 2025/09/19 17:24
# leetgo: 1.4.15
# https://leetcode.cn/problems/sum-of-all-subset-xor-totals/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        path = []
        n = len(nums)

        def xor():
            res = 0
            for v in path:
                res ^= v
            return res

        def dfs(i):
            # ans.append(path.copy())
            nonlocal ans
            ans += xor()
            if i == n:
                return
            for j in range(i, n):
                path.append(nums[j])
                dfs(j + 1)
                path.pop()

        dfs(0)
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().subsetXORSum(nums)
    print("\noutput:", serialize(ans, "integer"))
