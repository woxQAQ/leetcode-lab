# Created by woxQAQ at 2025/09/06 19:36
# leetgo: 1.4.15
# https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/

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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = None

        def dfs(node):
            if not node:
                return

            dfs(node.right)
            dfs(node.left)
            node.left = None
            nonlocal pre
            node.right = pre
            pre = node

        dfs(root)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    flatten(root)
    ans = root
    print("\noutput:", serialize(ans, "TreeNode"))
