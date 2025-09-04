# Created by woxQAQ at 2025/09/03 21:23
# leetgo: 1.4.13
# https://leetcode.cn/problems/boats-to-save-people/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        l, r = 0, len(people) - 1
        boats = 0
        while l <= r:
            # if people[l] == limit:
            #     boats += 1
            #     l += 1
            #     continue
            tmp = people[l] + people[r]
            if tmp <= limit:
                r -= 1
                tmp += people[r]
            boats += 1
            l += 1
        return boats


# @lc code=end

if __name__ == "__main__":
    people: List[int] = deserialize("List[int]", read_line())
    limit: int = deserialize("int", read_line())
    ans = Solution().numRescueBoats(people, limit)
    print("\noutput:", serialize(ans, "integer"))
