# Created by woxQAQ at 2025/09/06 10:25
# leetgo: 1.4.15
# https://leetcode.cn/problems/balanced-binary-tree/

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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            if l == -1 or r == -1 or abs(l - r) > 1:
                return -1
            return max(l, r) + 1

        return dfs(root) != -1


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().isBalanced(root)
    print("\noutput:", serialize(ans, "boolean"))
