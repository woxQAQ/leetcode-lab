# Created by woxQAQ at 2025/09/06 15:16
# leetgo: 1.4.15
# https://leetcode.cn/problems/kth-smallest-element-in-a-bst/

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            if not node:
                return -1

            left = dfs(node.left)
            if left != -1:
                return left
            nonlocal k
            k -= 1
            if k == 0:
                return node.val

            return dfs(node.right)

        return dfs(root)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kthSmallest(root, k)
    print("\noutput:", serialize(ans, "integer"))
