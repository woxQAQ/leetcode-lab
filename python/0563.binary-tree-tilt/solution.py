# Created by woxQAQ at 2025/09/06 13:05
# leetgo: 1.4.15
# https://leetcode.cn/problems/binary-tree-tilt/

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
    def findTilt(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            ans += abs(left - right)
            return left + right + node.val

        dfs(root)
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().findTilt(root)
    print("\noutput:", serialize(ans, "integer"))
