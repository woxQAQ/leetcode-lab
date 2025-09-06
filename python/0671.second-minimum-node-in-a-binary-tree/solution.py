# Created by woxQAQ at 2025/09/06 06:51
# leetgo: 1.4.15
# https://leetcode.cn/problems/second-minimum-node-in-a-binary-tree/

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
    def findSecondMinimumValue(self, roo: Optional[TreeNode]) -> int:
        ans = -1

        def inorder(node, cur):
            if not node:
                return
            nonlocal ans
            if node.val != cur:
                if ans == -1:
                    ans = node.val
                else:
                    ans = min(ans, node.val)
            inorder(node.left, cur)
            inorder(node.right, cur)

        inorder(roo, roo.val)
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().findSecondMinimumValue(root)
    print("\noutput:", serialize(ans, "integer"))
