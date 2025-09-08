# Created by woxQAQ at 2025/09/07 10:26
# leetgo: 1.4.15
# https://leetcode.cn/problems/number-of-provinces/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        vis = [False] * len(isConnected)
        ans = 0

        def dfs(i):
            vis[i] = True
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and not vis[j]:
                    dfs(j)

        for i in range(len(isConnected)):
            if not vis[i]:
                dfs(i)
                ans += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    isConnected: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findCircleNum(isConnected)
    print("\noutput:", serialize(ans, "integer"))
