# Created by woxQAQ at 2025/09/05 18:26
# leetgo: 1.4.15
# https://leetcode.cn/problems/leaf-similar-trees/

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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def inorder(node: Optional[TreeNode]) -> List[int]:
            if node is None:
                return []
            if node.left is None and node.right is None:
                return [node.val]
            return inorder(node.left) + inorder(node.right)

        return inorder(root1) == inorder(root2)


# @lc code=end

if __name__ == "__main__":
    root1: TreeNode = deserialize("TreeNode", read_line())
    root2: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().leafSimilar(root1, root2)
    print("\noutput:", serialize(ans, "boolean"))
