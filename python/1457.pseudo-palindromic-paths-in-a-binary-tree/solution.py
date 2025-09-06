# Created by woxQAQ at 2025/09/06 07:39
# leetgo: 1.4.15
# https://leetcode.cn/problems/pseudo-palindromic-paths-in-a-binary-tree/

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
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        path = [0] * 10

        def dfs(node):
            if not node:
                return 0
            path[node.val] ^= 1
            if not node.left and not node.right:
                res = 1 if sum(path) <= 1 else 0
            else:
                res = dfs(node.left) + dfs(node.right)
            path[node.val] ^= 1
            return res

        return dfs(root)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().pseudoPalindromicPaths(root)
    print("\noutput:", serialize(ans, "integer"))
