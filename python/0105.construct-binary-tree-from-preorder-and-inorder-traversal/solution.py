# Created by woxQAQ at 2025/09/06 15:37
# leetgo: 1.4.15
# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {x: i for i, x in enumerate(inorder)}

        def dfs(prel, prer, inl, inr):
            if prel == prer:
                return None
            ls = idx[preorder[prel]] - inl
            l = dfs(prel + 1, prel + 1 + ls, inl, inl + ls)
            r = dfs(prel + 1 + ls, prer, inl + ls + 1, inr)
            return TreeNode(preorder[prel], l, r)

        return dfs(0, len(preorder), 0, len(inorder))


# @lc code=end

if __name__ == "__main__":
    preorder: List[int] = deserialize("List[int]", read_line())
    inorder: List[int] = deserialize("List[int]", read_line())
    ans = Solution().buildTree(preorder, inorder)
    print("\noutput:", serialize(ans, "TreeNode"))
