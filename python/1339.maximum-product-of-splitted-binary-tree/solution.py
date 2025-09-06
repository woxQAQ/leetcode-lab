# Created by woxQAQ at 2025/09/06 14:48
# leetgo: 1.4.15
# https://leetcode.cn/problems/maximum-product-of-splitted-binary-tree/

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
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = []

        def dfs(node):
            if node is None:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            sums.append(l + r + node.val)
            return l + r + node.val

        dfs(root)
        total = sums[-1]
        return max((total - x) * x for x in sums) % (10**9 + 7)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().maxProduct(root)
    print("\noutput:", serialize(ans, "integer"))
