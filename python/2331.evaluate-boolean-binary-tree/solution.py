# Created by woxQAQ at 2025/09/06 13:48
# leetgo: 1.4.15
# https://leetcode.cn/problems/evaluate-boolean-binary-tree/

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
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node.left:
                return node.val == 1
            if node.val == 2:
                return dfs(node.left) or dfs(node.right)
            return dfs(node.left) and dfs(node.right)

        return dfs(root)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().evaluateTree(root)
    print("\noutput:", serialize(ans, "boolean"))
