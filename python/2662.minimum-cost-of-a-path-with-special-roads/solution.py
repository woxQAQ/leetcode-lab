# Created by woxQAQ at 2025/09/08 20:31
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-cost-of-a-path-with-special-roads/

from collections import defaultdict
from heapq import heappop, heappush
from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimumCost(
        self, start: List[int], target: List[int], specialRoads: List[List[int]]
    ) -> int:
        s = tuple(start)
        t = tuple(target)
        
        # Create mapping for special roads
        road_starts = {}
        for x1, y1, x2, y2, cost in specialRoads:
            if (x1, y1) not in road_starts:
                road_starts[(x1, y1)] = []
            road_starts[(x1, y1)].append((x2, y2, cost))
        
        dis = defaultdict(lambda: inf)
        dis[s] = 0
        h = [(0, s)]
        
        while h:
            dv, v = heappop(h)
            if dv > dis[v]:
                continue
            
            # Direct move to target
            if v != t:
                direct_cost = abs(t[0] - v[0]) + abs(t[1] - v[1])
                new_dis = dv + direct_cost
                if new_dis < dis[t]:
                    dis[t] = new_dis
                    heappush(h, (new_dis, t))
            
            # Move to special road starts
            for (x1, y1), roads in road_starts.items():
                if (x1, y1) != v:
                    move_cost = abs(x1 - v[0]) + abs(y1 - v[1])
                    new_dis = dv + move_cost
                    if new_dis < dis[(x1, y1)]:
                        dis[(x1, y1)] = new_dis
                        heappush(h, (new_dis, (x1, y1)))
            
            # Use special roads from current position
            if v in road_starts:
                for x2, y2, cost in road_starts[v]:
                    new_dis = dv + cost
                    if new_dis < dis[(x2, y2)]:
                        dis[(x2, y2)] = new_dis
                        heappush(h, (new_dis, (x2, y2)))
        
        return dis[t]


# @lc code=end

if __name__ == "__main__":
    start: List[int] = deserialize("List[int]", read_line())
    target: List[int] = deserialize("List[int]", read_line())
    specialRoads: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumCost(start, target, specialRoads)
    print("\noutput:", serialize(ans, "integer"))
