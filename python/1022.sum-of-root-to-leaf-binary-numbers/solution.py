# Created by woxQAQ at 2025/09/06 08:42
# leetgo: 1.4.15
# https://leetcode.cn/problems/sum-of-root-to-leaf-binary-numbers/

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
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if not node:
                return 0
            path = path * 2 + node.val
            if not node.left and not node.right:
                return path
            return dfs(node.left, path) + dfs(node.right, path)

        return dfs(root, 0)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().sumRootToLeaf(root)
    print("\noutput:", serialize(ans, "integer"))
