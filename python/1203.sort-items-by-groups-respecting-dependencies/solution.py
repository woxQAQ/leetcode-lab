# Created by woxQAQ at 2025/09/08 13:29
# leetgo: 1.4.15
# https://leetcode.cn/problems/sort-items-by-groups-respecting-dependencies/

from collections import deque
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def sortItems(
        self, n: int, m: int, group: List[int], beforeItems: List[List[int]]
    ) -> List[int]:
        NO_GROUP = -1
        max_group_id = m
        for p in range(n):
            if group[p] == NO_GROUP:
                group[p] = max_group_id
                max_group_id += 1

        def toposort(
            items: list[int], indegree: list[int], neighbors: list[list[int]]
        ):
            q = deque(i for i in items if indegree[i] == 0)
            ans = []
            while q:
                x = q.popleft()
                ans.append(x)
                for y in neighbors[x]:
                    indegree[y] -= 1
                    if indegree[y] == 0:
                        q.append(y)
            return ans

        p_indeg = [0] * n
        g_indeg = [0] * max_group_id
        p_neighbors = [[] for _ in range(n)]
        g_neighbors = [[] for _ in range(max_group_id)]
        g_projects = [[] for _ in range(max_group_id)]

        for project in range(n):
            g_projects[group[project]].append(project)

            for before in beforeItems[project]:
                if group[before] != group[project]:
                    g_indeg[group[project]] += 1
                    g_neighbors[group[before]].append(group[project])
                else:
                    p_indeg[project] += 1
                    p_neighbors[before].append(project)

        ans = []
        group_queue = toposort(
            [i for i in range(max_group_id)], g_indeg, g_neighbors
        )

        if len(group_queue) != max_group_id:
            return []

        for group_id in group_queue:
            project_queue = toposort(g_projects[group_id], p_indeg, p_neighbors)
            if len(project_queue) != len(g_projects[group_id]):
                return []
            ans.extend(project_queue)

        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    m: int = deserialize("int", read_line())
    group: List[int] = deserialize("List[int]", read_line())
    beforeItems: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().sortItems(n, m, group, beforeItems)
    print("\noutput:", serialize(ans, "integer[]"))
