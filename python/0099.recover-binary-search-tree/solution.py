# Created by woxQAQ at 2025/09/06 17:55
# leetgo: 1.4.15
# https://leetcode.cn/problems/recover-binary-search-tree/

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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        a, b = None, None
        prev = None

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nonlocal a, b, prev
            if prev and prev.val > node.val:
                if not a:
                    a = prev
                    b = node
                else:
                    b = node
            prev = node
            dfs(node.right)

        dfs(root)
        a.val, b.val = b.val, a.val


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    recoverTree(root)
    ans = root
    print("\noutput:", serialize(ans, "TreeNode"))
