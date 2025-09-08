# Created by woxQAQ at 2025/09/06 17:50
# leetgo: 1.4.15
# https://leetcode.cn/problems/all-elements-in-two-binary-search-trees/

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
    def getAllElements(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> List[int]:
        l1, l2 = [], []

        def dfs(node, l):
            if not node:
                return
            dfs(node.left, l)
            l.append(node.val)
            dfs(node.right, l)

        dfs(root1, l1)
        dfs(root2, l2)
        i, j = 0, 0
        m, n = len(l1), len(l2)
        res = [0] * (m + n)
        while i < m or j < n:
            if i == m:
                res[i + j] = l2[j]
                j += 1
            elif j == n:
                res[i + j] = l1[i]
                i += 1
            elif l1[i] < l2[j]:
                res[i + j] = l1[i]
                i += 1
            else:
                res[i + j] = l2[j]
                j += 1
        return res


# @lc code=end

if __name__ == "__main__":
    root1: TreeNode = deserialize("TreeNode", read_line())
    root2: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().getAllElements(root1, root2)
    print("\noutput:", serialize(ans, "integer[]"))
