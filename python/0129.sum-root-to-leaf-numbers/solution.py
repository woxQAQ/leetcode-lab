# Created by woxQAQ at 2025/09/06 07:31
# leetgo: 1.4.15
# https://leetcode.cn/problems/sum-root-to-leaf-numbers/

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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node, num):
            nonlocal ans
            if not node:
                return
            num = num * 10 + node.val
            if not node.left and not node.right:
                ans += num
            dfs(node.left, num)
            dfs(node.right, num)

        dfs(root, 0)
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().sumNumbers(root)
    print("\noutput:", serialize(ans, "integer"))
