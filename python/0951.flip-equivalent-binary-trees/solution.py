# Created by woxQAQ at 2025/09/06 10:14
# leetgo: 1.4.15
# https://leetcode.cn/problems/flip-equivalent-binary-trees/

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
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        return (
            self.flipEquiv(root1.left, root2.left)
            or self.flipEquiv(root1.left, root2.right)
            or self.flipEquiv(root1.right, root2.right)
            or self.flipEquiv(root1.right, root2.left)
        )


# @lc code=end

if __name__ == "__main__":
    root1: TreeNode = deserialize("TreeNode", read_line())
    root2: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().flipEquiv(root1, root2)
    print("\noutput:", serialize(ans, "boolean"))
