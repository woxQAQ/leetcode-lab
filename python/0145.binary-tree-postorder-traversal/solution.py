# Created by woxQAQ at 2025/09/05 18:26
# leetgo: 1.4.15
# https://leetcode.cn/problems/binary-tree-postorder-traversal/

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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return (
            self.postorderTraversal(root.left)
            + self.postorderTraversal(root.right)
            + [root.val]
        )


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().postorderTraversal(root)
    print("\noutput:", serialize(ans, "integer[]"))
