# Created by woxQAQ at 2025/09/06 11:51
# leetgo: 1.4.15
# https://leetcode.cn/problems/merge-two-binary-trees/

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
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root1 or not root2:
            return root1 or root2

        def dfs(node1, node2):
            if not node1 and not node2:
                return None
            if not node1:
                return node2
                # return TreeNode(val=node2.val)
            if not node2:
                return node1
            node = TreeNode(val=node1.val + node2.val)
            node.left = dfs(node1.left, node2.left)
            node.right = dfs(node1.right, node2.right)
            return node

        cur = dfs(root1, root2)
        return cur


# @lc code=end

if __name__ == "__main__":
    root1: TreeNode = deserialize("TreeNode", read_line())
    root2: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().mergeTrees(root1, root2)
    print("\noutput:", serialize(ans, "TreeNode"))
