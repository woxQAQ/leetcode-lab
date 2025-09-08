# Created by woxQAQ at 2025/09/07 11:55
# leetgo: 1.4.15
# https://leetcode.cn/problems/keys-and-rooms/

from collections import defaultdict
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vis = [False] * len(rooms)

        def dfs(i):
            if vis[i]:
                return
            vis[i] = True
            for j in rooms[i]:
                dfs(j)

        dfs(0)
        return all(vis)


# @lc code=end

if __name__ == "__main__":
    rooms: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().canVisitAllRooms(rooms)
    print("\noutput:", serialize(ans, "boolean"))
