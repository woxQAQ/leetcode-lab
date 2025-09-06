# Created by woxQAQ at 2025/09/06 09:59
# leetgo: 1.4.15
# https://leetcode.cn/problems/symmetric-tree/

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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or not root.left and not root.right:
            return True

        def dfs(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            return l.val == r.val and dfs(l.left, r.right) and dfs(l.right, r.left)

        return dfs(root.left, root.right)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().isSymmetric(root)
    print("\noutput:", serialize(ans, "boolean"))
