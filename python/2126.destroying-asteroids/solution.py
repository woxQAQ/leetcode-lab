# Created by woxQAQ at 2025/09/02 15:05
# leetgo: 1.4.13
# https://leetcode.cn/problems/destroying-asteroids/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for a in asteroids:
            if mass < a:
                return False
            mass += a
        return True


# @lc code=end

if __name__ == "__main__":
    mass: int = deserialize("int", read_line())
    asteroids: List[int] = deserialize("List[int]", read_line())
    ans = Solution().asteroidsDestroyed(mass, asteroids)
    print("\noutput:", serialize(ans, "boolean"))
