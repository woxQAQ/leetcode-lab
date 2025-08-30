# Created by woxQAQ at 2025/08/30 14:26
# leetgo: 1.4.13
# https://leetcode.cn/problems/closest-equal-element-queries/

from bisect import bisect_left
from collections import defaultdict
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        pos = defaultdict(list)
        n = len(nums)
        for i, num in enumerate(nums):
            pos[num].append(i)
        for p in pos.values():
            p.insert(0, p[-1] - n)
            p.append(p[1] + n)
        # [1,3,1,4,1,3,2]
        # {1:[0,2,4], 2:[6], 3:[1,5], 4:[3]}
        # query = [0,3,5]
        #
        # for q in queries
        #   [0,2,4]
        #   p = pos[nums[q]]
        #   i =  bisect_left(p, q) = 0
        #   min(p[(len(p)+i-1) % len(p)]-0, p[(len(p)+i+1) % len(p)]-0)
        ans = []
        for q in queries:
            p = pos[nums[q]]
            n = len(p)
            if n == 3:
                ans.append(-1)
                continue
            i = bisect_left(p, q)
            ans.append(min(q - p[i - 1], p[i + 1] - q))
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    queries: List[int] = deserialize("List[int]", read_line())
    ans = Solution().solveQueries(nums, queries)
    print("\noutput:", serialize(ans, "integer[]"))
