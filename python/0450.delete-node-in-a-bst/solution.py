# Created by woxQAQ at 2025/09/06 19:46
# leetgo: 1.4.15
# https://leetcode.cn/problems/delete-node-in-a-bst/

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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def search(node):
            if not node:
                return None
            if node.val > key:
                node.left = search(node.left)
            elif node.val < key:
                node.right = search(node.right)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                t = node.left
                while t.right:
                    t = t.right
                t.right = node.right
                return node.left
            return node

        return search(root)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    key: int = deserialize("int", read_line())
    ans = Solution().deleteNode(root, key)
    print("\noutput:", serialize(ans, "TreeNode"))
