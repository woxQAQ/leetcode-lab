# Created by woxQAQ at 2025/09/06 15:03
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-distance-between-bst-nodes/

from math import inf
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
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans = inf
        prev = -inf

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nonlocal ans, prev
            ans = min(ans, node.val - prev)
            prev = node.val
            dfs(node.right)

        dfs(root)
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().minDiffInBST(root)
    print("\noutput:", serialize(ans, "integer"))
