# Created by woxQAQ at 2025/09/06 17:21
# leetgo: 1.4.15
# https://leetcode.cn/problems/diameter-of-binary-tree/

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            if not node:
                return -1
            l = dfs(node.left) + 1
            r = dfs(node.right) + 1
            nonlocal ans
            ans = max(ans, l + r)
            return max(l, r)

        dfs(root)
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().diameterOfBinaryTree(root)
    print("\noutput:", serialize(ans, "integer"))
