# Created by woxQAQ at 2025/09/06 07:25
# leetgo: 1.4.15
# https://leetcode.cn/problems/path-sum/

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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, s):
            if not node:
                return False
            if not node.left and not node.right:
                return s + node.val == targetSum
            return dfs(node.left, s + node.val) or dfs(node.right, s + node.val)

        return dfs(root, 0)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    targetSum: int = deserialize("int", read_line())
    ans = Solution().hasPathSum(root, targetSum)
    print("\noutput:", serialize(ans, "boolean"))
