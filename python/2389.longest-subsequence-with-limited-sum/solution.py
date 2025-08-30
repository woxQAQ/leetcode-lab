# Created by woxQAQ at 2025/08/30 04:39
# leetgo: 1.4.13
# https://leetcode.cn/problems/longest-subsequence-with-limited-sum/

from bisect import bisect_left
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        nums.sort()
        presum = [0] * (len(nums) + 1)
        # [1,3,7,12]
        for i in range(len(nums)):
            presum[i + 1] = presum[i] + nums[i]
        for q in queries:
            # x <= q => x < q + 1
            ans.append(bisect_left(presum, q + 1) - 1)

        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    queries: List[int] = deserialize("List[int]", read_line())
    ans = Solution().answerQueries(nums, queries)
    print("\noutput:", serialize(ans, "integer[]"))
