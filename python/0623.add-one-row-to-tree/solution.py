# Created by woxQAQ at 2025/09/06 09:04
# leetgo: 1.4.15
# https://leetcode.cn/problems/add-one-row-to-tree/

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
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)

        def dfs(node, d, father):
            if d == depth:
                if father.left is node:
                    father.left = TreeNode(val, left=node)
                elif father.right is node:
                    father.right = TreeNode(val, right=node)
            if not node:
                return
            dfs(node.left, d + 1, node)
            dfs(node.right, d + 1, node)

        dfs(root, 1, None)
        return root


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    val: int = deserialize("int", read_line())
    depth: int = deserialize("int", read_line())
    ans = Solution().addOneRow(root, val, depth)
    print("\noutput:", serialize(ans, "TreeNode"))
