# Created by woxQAQ at 2025/09/06 19:26
# leetgo: 1.4.15
# https://leetcode.cn/problems/increasing-order-search-tree/

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
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = dummy = TreeNode(val=0)

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            node.left = None
            nonlocal cur
            cur.right = node
            cur = node
            dfs(node.right)
            return dummy.right

        dfs(root)
        return dummy.right


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().increasingBST(root)
    print("\noutput:", serialize(ans, "TreeNode"))
