# Created by woxQAQ at 2025/09/19 17:17
# leetgo: 1.4.15
# https://leetcode.cn/problems/subsets/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)

        def dfs(i):
            ans.append(path.copy())
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
    ans = Solution().subsets(nums)
    print("\noutput:", serialize(ans, "integer[][]"))
