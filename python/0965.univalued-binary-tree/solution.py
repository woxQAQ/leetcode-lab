# Created by woxQAQ at 2025/09/06 10:05
# leetgo: 1.4.15
# https://leetcode.cn/problems/univalued-binary-tree/

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
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        val = root.val
        if root.left and (val != root.left.val or not self.isUnivalTree(root.left)):
            return False
        if root.right and (val != root.right.val or not self.isUnivalTree(root.right)):
            return False
        return True


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().isUnivalTree(root)
    print("\noutput:", serialize(ans, "boolean"))
