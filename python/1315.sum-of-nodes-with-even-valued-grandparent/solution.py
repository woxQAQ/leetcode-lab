# Created by woxQAQ at 2025/09/06 07:47
# leetgo: 1.4.15
# https://leetcode.cn/problems/sum-of-nodes-with-even-valued-grandparent/

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
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent, grandparent):
            if not node:
                return 0
            res = dfs(node.left, node, parent) + dfs(node.right, node, parent)
            if grandparent and grandparent.val % 2 == 0:
                res += node.val
            return res

        return dfs(root, None, None)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().sumEvenGrandparent(root)
    print("\noutput:", serialize(ans, "integer"))
