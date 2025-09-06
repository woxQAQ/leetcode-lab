# Created by woxQAQ at 2025/09/06 14:55
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-absolute-difference-in-bst/

from math import inf
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 二叉搜索树的中序遍历是递增的
        res = inf
        prev = -inf

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nonlocal res, prev
            res = min(res, node.val - prev)
            prev = node.val
            dfs(node.right)

        dfs(root)
        return res


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().getMinimumDifference(root)
    print("\noutput:", serialize(ans, "integer"))
