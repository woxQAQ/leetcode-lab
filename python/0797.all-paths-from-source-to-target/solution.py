# Created by woxQAQ at 2025/09/07 10:48
# leetgo: 1.4.15
# https://leetcode.cn/problems/all-paths-from-source-to-target/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(i):
            if i == len(graph) - 1:
                return [[i]]
            paths = []
            for j in graph[i]:
                for path in dfs(j):
                    paths.append([i] + path)
            return paths

        return dfs(0)


# @lc code=end

if __name__ == "__main__":
    graph: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().allPathsSourceTarget(graph)
    print("\noutput:", serialize(ans, "integer[][]"))
