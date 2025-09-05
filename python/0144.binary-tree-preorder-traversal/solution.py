# Created by woxQAQ at 2025/09/05 18:24
# leetgo: 1.4.15
# https://leetcode.cn/problems/binary-tree-preorder-traversal/

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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return (
            [root.val]
            + self.preorderTraversal(root.left)
            + self.preorderTraversal(root.right)
        )


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().preorderTraversal(root)
    print("\noutput:", serialize(ans, "integer[]"))
