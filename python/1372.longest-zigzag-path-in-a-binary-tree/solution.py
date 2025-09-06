# Created by woxQAQ at 2025/09/06 09:21
# leetgo: 1.4.15
# https://leetcode.cn/problems/longest-zigzag-path-in-a-binary-tree/

from functools import cache
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
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        RIGHT = 1
        LEFT = 0

        @cache
        def dfs(node, dir, length):
            if not node:
                return
            nonlocal ans
            ans = max(ans, length)
            if dir == RIGHT:
                dfs(node.right, LEFT, length + 1)
                dfs(node.left, RIGHT, 1)
            else:
                dfs(node.left, RIGHT, length + 1)
                dfs(node.right, LEFT, 1)

        dfs(root, RIGHT, 0)
        dfs(root, LEFT, 0)
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().longestZigZag(root)
    print("\noutput:", serialize(ans, "integer"))
