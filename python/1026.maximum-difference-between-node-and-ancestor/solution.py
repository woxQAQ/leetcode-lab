# Created by woxQAQ at 2025/09/06 08:39
# leetgo: 1.4.15
# https://leetcode.cn/problems/maximum-difference-between-node-and-ancestor/

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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        V = 0

        def dfs(node, min_val, max_val):
            if not node:
                return
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)
            nonlocal V
            V = max(V, max_val - min_val)
            dfs(node.left, min_val, max_val)
            dfs(node.right, min_val, max_val)

        dfs(root, root.val, root.val)
        return V


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().maxAncestorDiff(root)
    print("\noutput:", serialize(ans, "integer"))
