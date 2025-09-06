# Created by woxQAQ at 2025/09/06 14:24
# leetgo: 1.4.15
# https://leetcode.cn/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

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
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        ans = []

        def dfs(node):
            if node is None:
                return 0
            lh = dfs(node.left)
            rh = dfs(node.right)
            if lh < 0 or lh != rh:
                return -1
            ans.append(lh + 1)
            return lh + 1

        dfs(root)
        if k > len(ans):
            return -1
        ans.sort()
        return (1 << ans[-k]) - 1


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kthLargestPerfectSubtree(root, k)
    print("\noutput:", serialize(ans, "integer"))
