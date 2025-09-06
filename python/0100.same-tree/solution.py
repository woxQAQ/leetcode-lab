# Created by woxQAQ at 2025/09/06 09:54
# leetgo: 1.4.15
# https://leetcode.cn/problems/same-tree/

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif p and q:
            return (
                self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
                and p.val == q.val
            )
        # elif p or q:
        else:
            return False


# @lc code=end

if __name__ == "__main__":
    p: TreeNode = deserialize("TreeNode", read_line())
    q: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().isSameTree(p, q)
    print("\noutput:", serialize(ans, "boolean"))
