# Created by woxQAQ at 2025/09/07 13:39
# leetgo: 1.4.15
# https://leetcode.cn/problems/remove-methods-from-project/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        g = DefaultDict(list)
        for i, j in invocations:
            g[i].append(j)
        s = set()

        def dfs(i):
            if i in s:
                return
            s.add(i)
            for j in g[i]:
                if j not in s:
                    dfs(j)

        dfs(k)
        for x, y in invocations:
            if x not in s and y in s:
                return list(range(n))
        return list(set(range(n)) - s)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    invocations: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().remainingMethods(n, k, invocations)
    print("\noutput:", serialize(ans, "integer[]"))
