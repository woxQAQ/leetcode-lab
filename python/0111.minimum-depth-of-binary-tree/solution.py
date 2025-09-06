# Created by woxQAQ at 2025/09/06 07:24
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-depth-of-binary-tree/

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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, d):
            if not node:
                return d
            if not node.left and not node.right:
                return d + 1
            if not node.left:
                return dfs(node.right, d + 1)
            if not node.right:
                return dfs(node.left, d + 1)
            return min(dfs(node.left, d + 1), dfs(node.right, d + 1))

        return dfs(root, 0)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().minDepth(root)
    print("\noutput:", serialize(ans, "integer"))
