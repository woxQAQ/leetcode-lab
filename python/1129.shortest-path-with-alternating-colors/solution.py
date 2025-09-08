# Created by woxQAQ at 2025/09/08 09:46
# leetgo: 1.4.15
# https://leetcode.cn/problems/shortest-path-with-alternating-colors/

from collections import deque
from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        bg = [[] for _ in range(n)]
        rg = [[] for _ in range(n)]
        for x, y in redEdges:
            rg[x].append(y)
        for x, y in blueEdges:
            bg[x].append(y)
        
        visited = [[False, False] for _ in range(n)]
        ans = [-1] * n
        ans[0] = 0
        q = deque()
        
        for nxt in rg[0]:
            visited[nxt][0] = True
            q.append((nxt, 0, 1))
        for nxt in bg[0]:
            visited[nxt][1] = True
            q.append((nxt, 1, 1))
        
        while q:
            node, color, dist = q.popleft()
            if ans[node] == -1 or dist < ans[node]:
                ans[node] = dist
            
            if color == 0:
                for nxt in bg[node]:
                    if not visited[nxt][1]:
                        visited[nxt][1] = True
                        q.append((nxt, 1, dist + 1))
            else:
                for nxt in rg[node]:
                    if not visited[nxt][0]:
                        visited[nxt][0] = True
                        q.append((nxt, 0, dist + 1))
        
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    redEdges: List[List[int]] = deserialize("List[List[int]]", read_line())
    blueEdges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().shortestAlternatingPaths(n, redEdges, blueEdges)
    print("\noutput:", serialize(ans, "integer[]"))
