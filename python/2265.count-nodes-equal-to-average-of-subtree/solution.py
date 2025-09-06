# Created by woxQAQ at 2025/09/06 14:14
# leetgo: 1.4.15
# https://leetcode.cn/problems/count-nodes-equal-to-average-of-subtree/

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
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node):
            if not node:
                return 0, 0
            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)
            if node.val == (ls + rs + node.val) // (lc + rc + 1):
                nonlocal ans
                ans += 1
            return ls + rs + node.val, lc + rc + 1

        dfs(root)
        return ans


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().averageOfSubtree(root)
    print("\noutput:", serialize(ans, "integer"))
