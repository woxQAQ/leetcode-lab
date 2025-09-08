# Created by woxQAQ at 2025/09/07 14:59
# leetgo: 1.4.15
# https://leetcode.cn/problems/course-schedule/

from collections import defaultdict
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        indegree = [0] * numCourses

        for u, v in prerequisites:
            g[v].append(u)
            indegree[u] += 1

        q = [i for i in range(numCourses) if indegree[i] == 0]
        while q:
            for _ in range(len(q)):
                u = q.pop()
                for v in g[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)
            if not q:
                break
        return not any(indegree)


# @lc code=end

if __name__ == "__main__":
    numCourses: int = deserialize("int", read_line())
    prerequisites: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().canFinish(numCourses, prerequisites)
    print("\noutput:", serialize(ans, "boolean"))
