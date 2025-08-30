# Created by woxQAQ at 2025/08/30 17:09
# leetgo: 1.4.13
# https://leetcode.cn/problems/most-beautiful-item-for-each-query/

from bisect import bisect, bisect_left, bisect_right
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])
        for i in range(1, len(items)):
            items[i][1] = max(items[i][1], items[i - 1][1])

        ans = []
        for q in queries:
            # <= => > -1
            i = bisect_right(items, q, key=lambda x: x[0]) - 1
            if i >= 0:
                ans.append(items[i][1])
            else:
                ans.append(0)

        return ans


# @lc code=end

if __name__ == "__main__":
    items: List[List[int]] = deserialize("List[List[int]]", read_line())
    queries: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumBeauty(items, queries)
    print("\noutput:", serialize(ans, "integer[]"))
