# Created by woxQAQ at 2025/09/06 07:37
# leetgo: 1.4.15
# https://leetcode.cn/problems/count-good-nodes-in-binary-tree/

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
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            res = 1 if node.val >= max_val else 0
            res += dfs(node.left, max(max_val, node.val))
            res += dfs(node.right, max(max_val, node.val))
            return res

        return dfs(root, float("-inf"))


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().goodNodes(root)
    print("\noutput:", serialize(ans, "integer"))
