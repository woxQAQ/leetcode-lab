# Created by woxQAQ at 2025/09/07 15:14
# leetgo: 1.4.15
# https://leetcode.cn/problems/accounts-merge/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        g = DefaultDict(list)

        for i, account in enumerate(accounts):
            for mail in account[1:]:
                g[mail].append(i)

        def dfs(i):
            vis[i] = True
            for mail in accounts[i][1:]:
                if mail in s:
                    continue
                s.add(mail)
                for j in g[mail]:
                    if not vis[j]:
                        dfs(j)

        ans = []
        vis = [False] * len(accounts)
        for i in range(len(accounts)):
            if not vis[i]:
                s = set()
                dfs(i)
                ans.append([accounts[i][0]] + sorted(s))

        return ans


# @lc code=end

if __name__ == "__main__":
    accounts: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().accountsMerge(accounts)
    print("\noutput:", serialize(ans, "string[][]"))
