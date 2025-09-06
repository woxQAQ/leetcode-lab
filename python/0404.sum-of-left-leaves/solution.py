# Created by woxQAQ at 2025/09/06 06:50
# leetgo: 1.4.15
# https://leetcode.cn/problems/sum-of-left-leaves/

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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def inorder(node, isLeft):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return node.val if isLeft else 0
            return inorder(node.left, True) + inorder(node.right, False)

        return inorder(root, False)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().sumOfLeftLeaves(root)
    print("\noutput:", serialize(ans, "integer"))
