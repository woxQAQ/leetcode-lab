# Created by woxQAQ at 2025/09/06 17:46
# leetgo: 1.4.15
# https://leetcode.cn/problems/validate-binary-search-tree/

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None

        def dfs(node):
            if not node:
                return True
            if not dfs(node.left):
                return False
            nonlocal prev
            if prev and node.val <= prev.val:
                return False
            prev = node
            return dfs(node.right)

        return dfs(root)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().isValidBST(root)
    print("\noutput:", serialize(ans, "boolean"))
