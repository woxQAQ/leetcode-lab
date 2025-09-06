# Created by woxQAQ at 2025/09/06 14:10
# leetgo: 1.4.15
# https://leetcode.cn/problems/construct-string-from-binary-tree/

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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        if not root.left and not root.right:
            return str(root.val)
        l, r = self.tree2str(root.left), self.tree2str(root.right)
        return f"{root.val}({l})({r})" if r else f"{root.val}({l})"


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().tree2str(root)
    print("\noutput:", serialize(ans, "string"))
