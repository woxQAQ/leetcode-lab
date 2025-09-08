# Created by woxQAQ at 2025/09/08 12:08
# leetgo: 1.4.15
# https://leetcode.cn/problems/course-schedule-ii/

from collections import deque
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses
        g = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            g[y].append(x)
            indeg[x] += 1

        topo = []
        q = deque(i for i, d in enumerate(indeg) if d == 0)

        while q:
            x = q.popleft()
            topo.append(x)
            for y in g[x]:
                indeg[y] -= 1
                if indeg[y] == 0:
                    q.append(y)

        return topo if len(topo) == numCourses else []


# @lc code=end

if __name__ == "__main__":
    numCourses: int = deserialize("int", read_line())
    prerequisites: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findOrder(numCourses, prerequisites)
    print("\noutput:", serialize(ans, "integer[]"))
