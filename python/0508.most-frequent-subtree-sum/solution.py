# Created by woxQAQ at 2025/09/06 13:44
# leetgo: 1.4.15
# https://leetcode.cn/problems/most-frequent-subtree-sum/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        cnt = DefaultDict(int)

        def dfs(node):
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            s = l + r + node.val
            cnt[s] += 1
            return s

        dfs(root)
        max_freq = max(cnt.values())
        return [s for s, freq in cnt.items() if freq == max_freq]


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().findFrequentTreeSum(root)
    print("\noutput:", serialize(ans, "integer[]"))
